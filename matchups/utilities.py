import datetime
import pytz

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