from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from matchups import utilities
from django.contrib.auth.models import User
from matchups.forms import PickForm, TieBreakerForm

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