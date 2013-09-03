from django.shortcuts import render
from matchups.models import Matchup, Pick, TieBreaker, TieBreakerPick
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from matchups import utilities
from matchups.forms import PickForm, TieBreakerForm

def submit_picks_for_current_matchup(request):
    return submit_picks_for_week(request, utilities.current_week_number())

@login_required
def submit_picks_for_week(request, week_number):
    weeks = range(1,utilities.week_number_for_last_matchup())
    date_format = "%b %d"
    week_dates = str(utilities.start_date(week_number).strftime(date_format)) + " to " + str(utilities.end_date(week_number).strftime(date_format))
    matchup_list = None
    form_list = list()
    error_message = ''
    if utilities.has_first_matchup_of_week_started(week_number):
        error_message = 'Cannot change picks, first game of the week has already started.'
    else:
        matchup_list, tie_breaker_matchup = utilities.matchups_for_week(week_number)
        for matchup in matchup_list:
            form_list.append(create_form_for_matchup(matchup, request))
        if tie_breaker_matchup: 
            form_list.append(create_form_for_matchup(tie_breaker_matchup, request))
            form_list.append(create_form_for_tie_breaker(tie_breaker_matchup, request))
    context = {'matchup_list' : matchup_list,
               'form_list' : form_list,
               'error_message' : error_message,
               'week_number': int(week_number),
               'submitted_picks': request.method=="POST",
               'weeks' : weeks,
               'week_dates' : week_dates}
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

def scoreboard_current_week(request):
    return scoreboard_for_week(request, utilities.current_week_number())
    
def scoreboard_for_week(request, week_number):
    matchup_list, tie_breaker_matchup = utilities.matchups_for_week(week_number)
    user_list = list()
    if utilities.has_first_matchup_of_week_started(week_number):
        user_list = order_list(request.user, User.objects.all())
    elif request.user.is_authenticated():
        user_list.append(request.user)
    return scoreboard(request, matchup_list, tie_breaker_matchup, user_list, week_number)
    
def scoreboard(request, matchup_list, tie_breaker_matchup, user_list, week_number):
    selected_teams = list()
    for matchup in matchup_list:
        matchup_to_selections = MatchupToSelections(matchup, user_list)
        selected_teams.append(matchup_to_selections)
    if tie_breaker_matchup:
        tie_breaker_matchup_selections = TieBreakerMatchupSelections(tie_breaker_matchup, user_list)
    wins = calculate_wins(user_list, matchup_list, tie_breaker_matchup)
    weeks = range(1,utilities.week_number_for_last_matchup())
    date_format = "%b %d"
    week_dates = str(utilities.start_date(week_number).strftime(date_format)) + " to " + str(utilities.end_date(week_number).strftime(date_format))
    context = {'tie_breaker_matchup_selections': tie_breaker_matchup_selections,
               'users' : user_list,
               'selected_teams': selected_teams,
               'weeks': weeks,
               'selected_week': int(week_number),
               'week_dates': week_dates,
               'wins': wins}
    return render(request, 'scoreboard.html', context)

def calculate_wins(users, matchups, tie_breaker_matchup):
    win_list = list()
    for user in users:
        number_of_wins = number_of_wins_for_user(user, matchups, tie_breaker_matchup)
        win_list.append(number_of_wins)
    return win_list

def number_of_wins_for_user(user, matchups, tie_breaker_matchup):
    wins = 0
    for matchup in matchups:
        if picked_the_winning_team(user, matchup):
            wins += 1
    if tie_breaker_matchup and picked_the_winning_team(user, tie_breaker_matchup):
        wins += 1
    return wins

def picked_the_winning_team(user, matchup):
    picks_for_matchups = Pick.objects.filter(user=user, matchup=matchup)
    if picks_for_matchups.count() > 0:
        pick = picks_for_matchups[0]
        if pick.is_winning_pick():
            return True
    return False

def order_list(current_user, users):
    ordered_user_list = list()
    for user in users:
        if user == current_user:
            ordered_user_list.insert(0,user)
        else:
            ordered_user_list.append(user)
    return ordered_user_list
        
class MatchupToSelections(object):
    matchup = Matchup()
    picks = list()
    def __init__(self, matchup, users):
        self.matchup = matchup
        self.picks = list()
        for user in users:
            pick_list = Pick.objects.filter(matchup=matchup, user=user)
            if(pick_list.count() < 1):
                pick = None
            else:
                pick = pick_list[0]
            self.picks.append(pick)
            
class TieBreakerMatchupSelections(MatchupToSelections):
    def __init__(self, matchup, users):
        super(TieBreakerMatchupSelections, self).__init__(matchup, users)
        tie_breaker = TieBreaker.objects.get(matchup=matchup)
        self.tie_breaker_scores = list()
        for user in users:
            picks = TieBreakerPick.objects.filter(tie_breaker=tie_breaker,user=user)
            if(picks.count() < 1):
                predicted_total_score = ''
            else:
                predicted_total_score = picks[0].predicted_total_score
            self.tie_breaker_scores.append(predicted_total_score)
    tie_breaker_scores = list()

def current_matchups(request):
    return weekly_matchups(request, utilities.current_week_number())

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