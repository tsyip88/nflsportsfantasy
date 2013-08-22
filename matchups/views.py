from django.shortcuts import render
from matchups.models import Matchup, Pick
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from matchups import utilities
from matchups.forms import PickForm
                
def all_matchups(request):
    matchup_list = Matchup.objects.all()
    date_range = "All matchups"
    context = {'matchup_list' : matchup_list,
               'date_range' : date_range,}
    return render(request, 'matchups.html', context)

def weekly_matchups(request, week_number):
    if int(week_number) < 1:
        context = {'date_range' : 'Week number is invalid'}
        return render(request, 'matchups.html', context)
    start_date = utilities.start_date(week_number)
    end_date = utilities.end_date(week_number) 
    matchup_list = Matchup.objects.filter(date_time__gt=start_date, date_time__lt=end_date)
    date_range = 'From ' + str(start_date.date()) + ' to ' + str(end_date.date())
    context = {'matchup_list' : matchup_list,
               'date_range' : date_range,}
    return render(request, 'matchups.html', context)

def current_matchups(request):
    return weekly_matchups(request, utilities.current_week_number())
    
def get_or_create_pick(matchup, user):
    picks_for_matchup = Pick.objects.filter(matchup=matchup, user=user)
    if len(picks_for_matchup) > 0:
        pick = picks_for_matchup[0]
    else:
        pick = Pick(matchup=matchup, user=user)
    return pick
        
@login_required
def submit_picks(request):
    error_message = ''
    matchups = Matchup.objects.all()
    form_list = list()
    for matchup in matchups:
        pick = get_or_create_pick(matchup, request.user)
        if request.method == "POST":
            form = PickForm(request.POST, prefix=matchup.id, instance=pick)
            if form.is_valid():
                form.save()
        else:
            form = PickForm(instance=pick, prefix=matchup.id)
        form_list.append(form)
    context = {'matchups' : matchups,
               'form_list' : form_list,
               'error_message' : error_message}
    return render(request, 'submit_picks.html', context)
    
class MatchupToSelections:
    matchup = Matchup()
    selections = list()
    
def results(request, matchups):
    users = User.objects.all()
    selected_teams = list()
    for matchup in matchups:
        matchup_to_selections = MatchupToSelections()
        matchup_to_selections.matchup = matchup
        
        for user in users:
            picks = Pick.objects.filter(matchup__id=matchup.id, user__id=user.id)
            if(len(picks) < 1):
                selected_team = ''
            else:
                selected_team = picks[0].selected_team
            matchup_to_selections.selections.append(selected_team)
        selected_teams.append(matchup_to_selections)
    picks = Pick.objects.all()
    context = {'matchups': matchups,
               'users' : users,
               'selected_teams': selected_teams}
    return render(request, 'results.html', context)
    
def all_results(request):
    matchups = Matchup.objects.all()
    return results(request, matchups)

def current_results(request):
    return weekly_results(request, utilities.current_week_number())
    
def weekly_results(request, week_number):
    start_date = utilities.start_date(week_number)
    end_date = utilities.end_date(week_number)
    matchups = Matchup.objects.filter(date_time__gt=start_date, date_time__lt=end_date)
    return results(request, matchups)