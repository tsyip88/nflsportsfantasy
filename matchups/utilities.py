import datetime
import pytz
from matchups.models import Matchup, TieBreaker, Pick, TieBreakerPick

DAYS_IN_A_WEEK = 7

def week_1_start_datetime():
    return datetime.datetime(year=2013, month=9, day=5, tzinfo=pytz.timezone('US/Mountain'))

def start_date(week_number):
    offset_from_week_1 = datetime.timedelta(weeks = int(week_number)-1)
    start_date = week_1_start_datetime() + offset_from_week_1
    return start_date
    
def end_date(week_number):
    end_date = start_date(week_number) + datetime.timedelta(weeks=1)
    return end_date

def current_week_number():
    time_elapsed_since_week_1 = datetime.datetime.now(pytz.timezone('US/Mountain'))-week_1_start_datetime()
    if(time_elapsed_since_week_1.total_seconds() < 0):
        return 1
    else:
        return (int(time_elapsed_since_week_1.days)/DAYS_IN_A_WEEK) + 1
    
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
        print str(tie_breaker_matchup.id)
        tie_breaker = TieBreaker.objects.get(matchup__id=tie_breaker_matchup.id)
        pick = TieBreakerPick(tie_breaker=tie_breaker, user=user)
    return pick