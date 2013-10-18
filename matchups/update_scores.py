from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from matchups.forms import MatchupForm
from matchups import utilities

def update_current_scores(request):
    return update_scores_for_week(request, utilities.current_week_number())

@permission_required('matchups.add_matchup')
def update_scores_for_week(request, week_number):
    weeks = range(1,utilities.week_number_for_last_matchup()+1)
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
