from django.shortcuts import render
from matchups import utilities

def current_matchups(request):
    return weekly_matchups(request, utilities.current_week_number())

def weekly_matchups(request, week_number):
    if int(week_number) < 1:
        context = {'date_range' : 'Week number is invalid'}
        return render(request, 'matchup_list.html', context)
    start_date = utilities.start_date(week_number)
    end_date = utilities.end_date(week_number)
    matchup_list, tie_breaker_matchup = utilities.matchups_for_week(week_number)
    date_range = 'From ' + str(start_date.date()) + ' to ' + str(end_date.date())
    context = {'matchup_list' : matchup_list,
               'tie_breaker_matchup' : tie_breaker_matchup,
               'date_range' : date_range,}
    return render(request, 'matchup_list.html', context)