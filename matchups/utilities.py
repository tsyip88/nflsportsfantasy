import datetime
import pytz
import math
from matchups.models import Matchup, TieBreaker, Pick, TieBreakerPick
from django.contrib.auth.models import User

DAYS_IN_A_WEEK = 7

def week_1_start_datetime():
    return datetime.datetime(year=2013, month=9, day=4, tzinfo=pytz.timezone('US/Mountain'))

def start_date(week_number):
    offset_from_week_1 = datetime.timedelta(weeks = int(week_number)-1)
    start_date = week_1_start_datetime() + offset_from_week_1
    return start_date
    
def end_date(week_number):
    end_date = start_date(week_number) + datetime.timedelta(weeks=1)
    return end_date

def week_is_over(week_number):
    start = start_date(week_number)
    end = end_date(week_number)
    matchups = Matchup.objects.filter(date_time__gt=start,date_time__lt=end, home_team_score=-1, away_team_score=-1)
    return matchups.count()==0

def current_week_number():
    time_elapsed_since_week_1 = datetime.datetime.now(pytz.timezone('US/Mountain'))-week_1_start_datetime()
    if(time_elapsed_since_week_1.total_seconds() < 0):
        return 1
    else:
        return (int(time_elapsed_since_week_1.days)/DAYS_IN_A_WEEK) + 1
    
def week_number_for_last_matchup():
    matchups = Matchup.objects.all().order_by('date_time')
    if matchups.count() > 0:
        return week_number_for_matchup(matchups[matchups.count()-1])
    return -1

def week_number_for_matchup(matchup):
    matchup_date = matchup.date_time
    offset_from_week_1 = matchup_date - week_1_start_datetime()
    week_number = math.floor((offset_from_week_1.days/DAYS_IN_A_WEEK))+1
    return int(week_number)
    
def matchups_for_week(week_number):
    start = start_date(week_number)
    end = end_date(week_number)
    tie_breakers = TieBreaker.objects.filter(matchup__date_time__gt=start, matchup__date_time__lt=end)
    if tie_breakers.count() > 0:
        tie_breaker_matchup = tie_breakers[0].matchup
        matchups = Matchup.objects.filter(date_time__gt=start, date_time__lt=end).exclude(id=tie_breaker_matchup.id)
    else:
        tie_breaker_matchup = None
        matchups = Matchup.objects.filter(date_time__gt=start, date_time__lt=end)
        
    return matchups, tie_breaker_matchup
    
def users_that_have_submitted_picks_for_week(week_number):
    user_list = list()
    start = start_date(week_number)
    end = end_date(week_number)
    for user in User.objects.all():
        if Pick.objects.filter(user=user, matchup__date_time__gt=start, matchup__date_time__lt=end).count() > 0:
            user_list.append(user)
    return user_list
    
def get_or_create_pick(matchup, user):
    picks_for_matchup = Pick.objects.filter(matchup=matchup, user=user)
    if picks_for_matchup.count() > 0:
        pick = picks_for_matchup[0]
    else:
        pick = Pick(matchup=matchup, user=user)
    return pick

def get_or_create_tie_breaker_pick(tie_breaker_matchup, user):
    picks_for_tie_breakers = TieBreakerPick.objects.filter(tie_breaker__matchup=tie_breaker_matchup, user=user)
    if picks_for_tie_breakers.count() > 0:
        pick = picks_for_tie_breakers[0]
    else:
        tie_breaker = TieBreaker.objects.get(matchup=tie_breaker_matchup)
        pick = TieBreakerPick(tie_breaker=tie_breaker, user=user)
    return pick

def datetime_for_first_matchup(week_number):
    start = start_date(week_number)
    end = end_date(week_number)
    matchups = Matchup.objects.filter(date_time__gt=start, date_time__lt=end).order_by('date_time')
    if matchups.count() > 0:
        return matchups[0].date_time
    return None

def has_first_matchup_of_week_started(week_number):
    return datetime.datetime.now(pytz.timezone('UTC')) > datetime_for_first_matchup(week_number)