from django.shortcuts import render
from matchups.models import Matchup, Pick, TieBreaker
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from matchups import utilities
from matchups.forms import PickForm, TieBreakerForm
                
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
    matchup_list, tie_breaker_matchup = utilities.matchups_for_week(week_number)
    date_range = 'From ' + str(start_date.date()) + ' to ' + str(end_date.date())
    context = {'matchup_list' : matchup_list,
               'tie_breaker_matchup' : tie_breaker_matchup,
               'date_range' : date_range,}
    return render(request, 'matchups.html', context)

def current_matchups(request):
    return weekly_matchups(request, utilities.current_week_number())

def submit_picks_for_current_matchup(request):
    return submit_picks_for_week(request, utilities.current_week_number())

@login_required
def submit_picks_for_week(request, week_number):
    matchup_list, tie_breaker_matchup = utilities.matchups_for_week(week_number)
    error_message = ''
    form_list = list()
    for matchup in matchup_list:
        form = create_form_for_matchup(matchup, request)
        form_list.append(form)
        
    if tie_breaker_matchup:
        form = create_form_for_matchup(tie_breaker_matchup, request)
        form_list.append(form)
        form = create_form_for_tie_breaker(tie_breaker_matchup, request)
        form_list.append(form)
    context = {'matchup_list' : matchup_list,
               'form_list' : form_list,
               'error_message' : error_message}
    return render(request, 'submit_picks.html', context)

def create_form_for_matchup(matchup, request):
    pick = utilities.get_or_create_pick(matchup, request.user)
    if request.method == "POST":
        form = PickForm(request.POST, prefix=matchup.id, instance=pick)
        if form.is_valid():
            form.save()
    else:
        form = PickForm(instance=pick, prefix=matchup.id)
    return form

def create_form_for_tie_breaker(tie_breaker_matchup, request):
    tie_breaker_pick = utilities.get_or_create_tie_breaker_pick(tie_breaker_matchup, request.user)
    if request.method == "POST":
        form = TieBreakerForm(request.POST, instance=tie_breaker_pick)
        if form.is_valid():
            form.save()
    else:
        form = TieBreakerForm(instance=tie_breaker_pick)
    return form
        
class MatchupToSelections:
    matchup = Matchup()
    selections = list()
    
def results(request, matchup_list, tie_breaker_matchup):
    users = User.objects.all()
    selected_teams = list()
    
    if tie_breaker_matchup:
        matchup_list.append(tie_breaker_matchup)
    for matchup in matchup_list:
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
    context = {'matchup_list': matchup_list,
               'tie_breaker_matchup': tie_breaker_matchup,
               'users' : users,
               'selected_teams': selected_teams}
    return render(request, 'results.html', context)
    
def all_results(request):
    matchup_list = Matchup.objects.all()
    return results(request, matchup_list)

def current_results(request):
    return weekly_results(request, utilities.current_week_number())
    
def weekly_results(request, week_number):
    matchup_list, tie_breaker_matchup = utilities.matchups_for_week(week_number)
    return results(request, matchup_list, tie_breaker_matchup)