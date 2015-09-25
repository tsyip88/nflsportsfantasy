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
        for i in range(4,18):
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

class MatchupScheduleParser(HTMLParser):
    in_teams_field = False
    in_home_team_field = False
    matchups = list()
    last_retrieved_date = None
    home_team = None
    away_team = None
    date_time = None
    zulu = pytz.timezone('Etc/Zulu')
    mountain = pytz.timezone('US/Mountain')
    
    def handle_starttag(self, tag, attrs):        
        if tag == 'div' and self.attr_contains_val(attrs,'class','teams'):
            self.in_teams_field = True
            
        if tag == 'td':
            if self.attr_contains_val(attrs,'class','home'):
                self.in_home_team_field = True
            if self.attr_contains_val(attrs,'data-behavior','date_time'):
                date_time_string = self.attribute_value(attrs,'data-date')
                date_time = self.parse_date_time(date_time_string)
                current = datetime.datetime.now(pytz.timezone('US/Mountain'))
                timeDiff = date_time - current
                print "Diff = "
                print timeDiff
                if date_time:
                    self.date_time = date_time
        
        if tag == 'tr':
            self.home_team = None
            self.away_team = None
            self.date_time = None
            
    def handle_data(self, data):
        if self.in_teams_field:
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
            
    def handle_endtag(self, tag):     
        if tag == 'span':
            self.in_teams_field = False            
        if tag == 'td':
            self.in_home_team_field = False
            self.in_date_field = False
        if tag == 'tr':
            self.save_matchup_if_have_valid_data()
            
    def attr_contains_val(self, attrs, attr_name, attr_value):
        for attr in attrs:
            if attr[0] == attr_name and string.find(attr[1], attr_value) > -1:
                return True
        return False
            
    def attribute_value(self, attrs, attr_name):
        for attr in attrs:
            if attr[0] == attr_name:
                return str(attr[1])
        return None
    
    def save_matchup_if_have_valid_data(self):
        if self.home_team and self.away_team and self.date_time:
            print "Saving as: %s, %s, %s" %(self.away_team,self.home_team, self.date_time)
            matchup = matchups.models.Matchup(home_team=self.home_team, away_team=self.away_team, date_time=self.date_time)
            matchup.save()  
                    
    def parse_date_time(self, data):
        search_results = re.search(r"(\d+)-(\d+)-(\d+)T(\d+):(\d+)Z", data)
        if search_results:
            year = int(search_results.group(1))
            month = int(search_results.group(2))
            day = int(search_results.group(3))
            hour = int(search_results.group(4))
            minute = int(search_results.group(5))
            parsed_date_time = datetime.datetime(year,
                                                 month,
                                                 day,
                                                 hour,
                                                 minute)
            return self.zulu.localize(parsed_date_time)
        else:
            print "Failed to parse"
            return None