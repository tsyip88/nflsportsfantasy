from django.shortcuts import render, redirect, get_object_or_404
from matchups.models import Matchup, Pick, TieBreaker, TieBreakerPick
from django.contrib.auth.decorators import login_required, permission_required
from matchups import utilities
from matchups.forms import PickForm, TieBreakerForm, MatchupForm
from django.contrib.auth.models import User
from django.db.models import Q, F

def submit_picks_for_current_matchup(request):
    return submit_picks_for_week(request, utilities.current_submit_picks_week_number())

@permission_required('matchups.add_matchup')
def admin_submit_picks_for_week(request, week_number, user_id):
    user = get_object_or_404(User, id=user_id)
    return submit_picks_for_user(request, week_number, user, True)

@login_required
def submit_picks_for_week(request, week_number):
    return submit_picks_for_user(request, week_number, request.user)

@login_required
def submit_picks_for_user(request, week_number, user, is_admin = False):
    if request.method =="POST" and request.POST.has_key('user_select'):
        selected_username = request.POST.get('user_select')
        selected_user = User.objects.get(username=selected_username)
        return redirect('matchups:admin_submit_picks_for_week', week_number=week_number, user_id=selected_user.id)
    weeks = range(1,utilities.week_number_for_last_matchup())
    date_format = "%b %d"
    week_dates = str(utilities.start_date(week_number).strftime(date_format)) + " to " + str(utilities.end_date(week_number).strftime(date_format))
    matchup_list = None
    form_list = list()
    error_message = ''
    if utilities.has_first_matchup_of_week_started(week_number) and not is_admin:
        error_message = 'Cannot change picks, first game of the week has already started.'
    else:
        matchup_list, tie_breaker_matchup = utilities.matchups_for_week(week_number)
        for matchup in matchup_list:
            form_list.append(create_form_for_matchup(matchup, request, user))
        if tie_breaker_matchup: 
            form_list.append(create_form_for_matchup(tie_breaker_matchup, request, user))
            form_list.append(create_form_for_tie_breaker(tie_breaker_matchup, request, user))
    context = {'matchup_list' : matchup_list,
               'form_list' : form_list,
               'error_message' : error_message,
               'week_number': int(week_number),
               'submitted_picks': request.method=="POST",
               'weeks' : weeks,
               'week_dates' : week_dates,
               'users' : User.objects.all(),
               'submit_user' : user,
               'is_admin' : is_admin}
    return render(request, 'submit_picks.html', context)

def create_form_for_matchup(matchup, request, user):
    pick = utilities.get_or_create_pick(matchup, user)
    if request.method == "POST":
        form = PickForm(request.POST, prefix=matchup.id, instance=pick)
        if form.is_valid():
            form.save()
    else:
        form = PickForm(instance=pick, prefix=matchup.id)
    return form

def create_form_for_tie_breaker(tie_breaker_matchup, request, user):
    tie_breaker_pick = utilities.get_or_create_tie_breaker_pick(tie_breaker_matchup, user)
    if request.method == "POST":
        form = TieBreakerForm(request.POST, instance=tie_breaker_pick)
        if form.is_valid():
            form.save()
    else:
        form = TieBreakerForm(instance=tie_breaker_pick)
    return form

def scoreboard_current_week(request):
    return scoreboard_for_week(request, utilities.current_week_number())

def update_current_scores(request):
    return update_scores_for_week(request, utilities.current_week_number())

@permission_required('matchups.add_matchup')
def update_scores_for_week(request, week_number):
    weeks = range(1,utilities.week_number_for_last_matchup())
    date_format = "%b %d"
    week_dates = str(utilities.start_date(week_number).strftime(date_format)) + " to " + str(utilities.end_date(week_number).strftime(date_format))
    forms = list()
    matchup_list, tie_breaker_matchup = utilities.matchups_for_week(week_number)
    for matchup in matchup_list:
        forms.append(create_form_for_matchup_scores(matchup, request))
    if tie_breaker_matchup:
        forms.append(create_form_for_matchup_scores(tie_breaker_matchup, request))
    context = {'weeks': weeks,
               'selected_week': int(week_number),
               'week_dates': week_dates,
               'forms': forms}
    return render(request, 'update_scores.html', context)

def create_form_for_matchup_scores(matchup, request):
    if request.method == "POST":
        matchup_form = MatchupForm(request.POST, instance=matchup, prefix=matchup.id)
        if matchup_form.is_valid():
            matchup_form.save()
    else:
        matchup_form = MatchupForm(instance=matchup, prefix=matchup.id)
    return matchup_form
    
@permission_required('matchups.add_matchup')
def admin_scoreboard_for_week(request, week_number):
    return scoreboard_for_week(request, week_number, True)
    
def scoreboard_for_week(request, week_number, is_admin=False):
    user_list = list()
    user = request.user
    if is_admin or utilities.has_first_matchup_of_week_started(week_number):
        user_list = order_list(user, utilities.users_that_have_submitted_picks_for_week(week_number))
    elif user.is_authenticated():
        user_list.append(user)
    return scoreboard(request, user_list, week_number, is_admin)
    
def scoreboard(request, user_list, week_number, is_admin=False):
    matchup_list, tie_breaker_matchup = utilities.matchups_for_week(week_number)
    selected_teams = list()
    for matchup in matchup_list:
        matchup_to_selections = MatchupToSelections(matchup, user_list)
        selected_teams.append(matchup_to_selections)
    wins = calculate_wins(user_list, week_number)
    if tie_breaker_matchup:
        tie_breaker_matchup_selections = TieBreakerMatchupSelections(tie_breaker_matchup, user_list)
    weeks = range(1,utilities.week_number_for_last_matchup())
    date_format = "%b %d"
    week_dates = str(utilities.start_date(week_number).strftime(date_format)) + " to " + str(utilities.end_date(week_number).strftime(date_format))
    winning_teams = list()
    if utilities.week_is_over(week_number):
        winning_teams = calculate_winners(wins, tie_breaker_matchup_selections)
    context = {'tie_breaker_matchup_selections': tie_breaker_matchup_selections,
               'users' : user_list,
               'selected_teams': selected_teams,
               'weeks': weeks,
               'selected_week': int(week_number),
               'week_dates': week_dates,
               'wins': wins,
               'winning_users': winning_teams,
               'is_admin': is_admin}
    return render(request, 'scoreboard.html', context)

def calculate_winners(wins, tie_breaker_matchup_selections):
    winning_teams = list()
    for win_to_user in wins:
        if win_to_user.has_most_number_of_wins:
            winning_teams.append(win_to_user.user)
    if len(winning_teams) > 1:
        winning_team_tie_breakers = list()
        tie_breaker_matchup = tie_breaker_matchup_selections.matchup
        actual_value = tie_breaker_matchup.home_team_score+tie_breaker_matchup.away_team_score
        for tie_breaker_score in tie_breaker_matchup_selections.tie_breaker_scores:
            if tie_breaker_score.user in winning_teams:
                winning_team_tie_breakers.append(tie_breaker_score)
                
        closest_diff_between_tie_breaker_and_actual = diff_between_scores(winning_team_tie_breakers[0].value, actual_value)
        for tie_breaker_score in winning_team_tie_breakers:
            difference = diff_between_scores(actual_value, tie_breaker_score.value) 
            if difference < closest_diff_between_tie_breaker_and_actual:
                closest_diff_between_tie_breaker_and_actual = difference
        winning_teams = list()        
        for tie_breaker_score in winning_team_tie_breakers:
            if diff_between_scores(actual_value, tie_breaker_score.value) == closest_diff_between_tie_breaker_and_actual:
                winning_teams.append(tie_breaker_score.user)
                tie_breaker_score.is_winning_tie_breaker = True
    return winning_teams

def diff_between_scores(first_score, second_score):
    return abs(first_score - second_score)

class WinsToUser(object):
    number_of_wins = 0
    user = None
    has_most_number_of_wins = False
    def __init__(self, num_wins, user):
        self.number_of_wins = num_wins
        self.user = user

def calculate_wins(users, week_number):
    wins_to_user_hash = dict()
    wins_to_user_list = list()
    start = utilities.start_date(week_number)
    end = utilities.end_date(week_number)
    for user in users:
        picks_for_matchups = Pick.objects.filter(Q(matchup__date_time__gt=start,
                                                   matchup__date_time__lt=end,
                                                   matchup__home_team_score__gt=-1,
                                                   user=user),
                                                 Q(matchup__home_team_score__gt=F('matchup__away_team_score'),
                                                   matchup__home_team=F('selected_team')) |
                                                 Q(matchup__away_team_score__gt=F('matchup__home_team_score'),
                                                   matchup__away_team=F('selected_team')))
        wins_to_user_hash[user] = picks_for_matchups.count()
    if len(wins_to_user_hash) == 0:
        most_wins = 0
    else:
        most_wins = max(wins_to_user_hash.values())
    for user in users:
        wins_to_user = WinsToUser(wins_to_user_hash[user], user)
        if most_wins > 0 and wins_to_user.number_of_wins == most_wins:
            wins_to_user.has_most_number_of_wins = True
        wins_to_user_list.append(wins_to_user)
    return wins_to_user_list

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
    current_user_pick = None
    def __init__(self, matchup, users):
        self.matchup = matchup
        self.picks = list()
        pick_list = Pick.objects.filter(matchup=matchup)
        pick_dict = dict()
        for pick in pick_list:
            pick_dict[pick.user] = pick
        for user in users:
            self.picks.append(pick_dict.get(user))

class TieBreakerScore(object):
    value = 0
    is_winning_tie_breaker = False
    user = None
    def __init__(self, score, user):
        self.value = score
        self.user = user
            
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
            self.tie_breaker_scores.append(TieBreakerScore(predicted_total_score, user))
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