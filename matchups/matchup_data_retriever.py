import matchups.models
import teams.models
import urllib
import time                                                                                                                                                                                             
from HTMLParser import HTMLParser
import datetime
import re
import string
import pytz

class MatchupDataRetriever:
    @staticmethod    
    def load_matchups():
        MatchupDataRetriever.clear_matchups()
        MatchupDataRetriever.load_matchup_at_url("http://espn.go.com/nfl/schedule")
        for i in range(2,18):
            url = "http://espn.go.com/nfl/schedule/_/week/" + str(i)
            MatchupDataRetriever.load_matchup_at_url(url)
    
    @staticmethod
    def load_matchup_at_url(url):
        contents, success = MatchupDataRetriever.retrieve_site_contents(url)        
        if not success:
            print "failed to load contents from: " + url
            return False
        successfully_processed = MatchupDataRetriever.process_data(contents)
        if successfully_processed:
            print "successfully loaded matchups"
            return True
        print "contents: " + str(contents)                                                                                                      
        return False
    
    @staticmethod
    def clear_matchups():
        matchup_list = matchups.models.Matchup.objects.all()
        for matchup in matchup_list:
            matchup.delete()

    @staticmethod
    def retrieve_site_contents(url):
        file_handle = urllib.urlopen(url)
        contents = file_handle.read()
        # This is necessary because espn has restricted the frequency of API calls to
        # 3 calls per second
        time.sleep(0.4)
        return contents, True

    @staticmethod
    def process_data(contents):
        html_processor = MatchupScheduleParser()
        html_processor.feed(contents)
        return True

DATE_FIELD_WIDTH = 170    
START_YEAR = 2014
MONTH_STRING_TO_INTEGER_HASH = {'JAN':1,
                                'FEB':2,
                                'MAR':3,
                                'APR':4,
                                'MAY':5,
                                'JUN':6,
                                'JUL':7,
                                'AUG':8,
                                'SEP':9,
                                'OCT':10,
                                'NOV':11,
                                'DEC':12,}
TEAMS_COLUMN = 1
TIME_COLUMN = 2

class MatchupScheduleParser(HTMLParser):
    in_colhead = False
    in_date_field = False
    matchups = list()
    last_retrieved_date = None
    in_matchup_row = False
    col_num = 0
    need_away_team = True
    home_team = None
    away_team = None
    date_time = None
    eastern = pytz.timezone('US/Eastern')
    mountain = pytz.timezone('US/Mountain')
    
    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            if self.attr_contains_val(attrs,'class','colhead'):
                self.in_colhead = True
            elif self.attr_contains_val(attrs, 'class', 'oddrow') or \
                 self.attr_contains_val(attrs, 'class', 'evenrow'):
                self.in_matchup_row = True
                self.home_team = None
                self.away_team = None
                self.date_time = None
            self.col_num = 0
            
        if tag == 'td':
            if self.in_colhead and self.attr_contains_val(attrs,'width',str(DATE_FIELD_WIDTH)):
                self.in_date_field = True
            self.col_num += 1
            
    def handle_data(self, data):
        if self.in_date_field:
            self.last_retrieved_date = self.parse_date(data)
        if self.in_matchup_row:
            if self.col_num == TEAMS_COLUMN:
                if data != ' at ':
                    all_teams = teams.models.Team.objects.all()
                    retrieved_team = None
                    for team in all_teams:
                        if team.schedule_lookup_name()==data:
                            retrieved_team = team
                            break 
                    if retrieved_team:
                        if self.away_team == None:
                            self.away_team = retrieved_team
                        else:
                            self.home_team = retrieved_team
            elif self.col_num == TIME_COLUMN:
                date_time = self.parse_date_time(data)
                if date_time:
                    self.date_time = date_time
            
    def handle_endtag(self, tag):
        if tag=='tr':
            if self.in_matchup_row:
                self.save_matchup_if_have_valid_data()
            self.in_colhead = False
            self.in_matchup_row = False
            self.col_num = 0
        if tag == 'td':
            self.in_date_field = False
            
    def attr_contains_val(self, attrs, attr_name, attr_value):
        for attr in attrs:
            if attr[0] == attr_name and string.find(attr[1], attr_value) > -1:
                return True
        return False
    
    def save_matchup_if_have_valid_data(self):
        if self.home_team and self.away_team and self.date_time:
            print "Saving as: %s, %s, %s" %(self.away_team,self.home_team, self.date_time)
            matchup = matchups.models.Matchup(home_team=self.home_team, away_team=self.away_team, date_time=self.date_time)
            matchup.save()
                        
    def parse_date(self, data):
        search_results = re.search(r"\w+, (\w+) (\d+)", data)
        if search_results:
            month = MONTH_STRING_TO_INTEGER_HASH.get(search_results.group(1))
            if month == 0:
                return None
            day = int(search_results.group(2))
            if month > 6:
                year = START_YEAR
            else:
                year = START_YEAR+1
            parsed_date = datetime.date(year, month, day)
            return parsed_date
        else:
            return None      
                    
    def parse_date_time(self, data):
        search_results = re.search(r"(\d+):(\d+) (\w+)", data)
        if not self.last_retrieved_date:
            return None
        if search_results:
            year = self.last_retrieved_date.year
            month = self.last_retrieved_date.month
            day = self.last_retrieved_date.day
            hour = int(search_results.group(1))
            minute = int(search_results.group(2))
            am_vs_pm = search_results.group(3)
            if am_vs_pm == 'PM':
                hour += 12
            if hour > 23:
                hour -= 12
            parsed_date_time = datetime.datetime(year,
                                                 month,
                                                 day,
                                                 hour,
                                                 minute)
            return self.eastern.localize(parsed_date_time)
        else:
            return None