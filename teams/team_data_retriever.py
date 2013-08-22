import teams.models
import urllib
import json
import time

class TeamDataRetriever:
    @staticmethod    
    def load_teams(sport_name, league_name):
        espnUrl = "http://api.espn.com/v1/sports/" + sport_name + "/" + league_name + "?apikey=qvf4w5he6tszff4j3y3ugvus"
        contents, success = TeamDataRetriever.retrieve_json_contents(espnUrl)        
        if success:
            successfully_extracted = TeamDataRetriever.extract_league_data(contents, sport_name, league_name)
            if successfully_extracted:
                print "successfully loaded league"
                return True
        print "failed to load teams, read from: " + espnUrl
        print "contents: " + str(contents)
        return False  

    @staticmethod
    def retrieve_json_contents(url):
        success = False
        file_handle = urllib.urlopen(url)
        json_data = file_handle.read()
        contents = json.loads(json_data)
        if contents['status'] == "success":
            success = True
        # This is necessary because espn has restricted the frequency of API calls to
        # 3 calls per second
        time.sleep(0.4)
        return contents, success

    @staticmethod
    def extract_league_data(contents, sport_name, league_name):
        print "-----------"
        extracted_league = contents['sports'][0]['leagues'][0]
        extracted_conferences = extracted_league['groups']
        
        new_league = teams.models.League()
        new_league.abbreviation = extracted_league['abbreviation'].upper()
        new_league.name = extracted_league['name']
        new_league.save()
        for extracted_conference in extracted_conferences:
            new_conference = teams.models.Conference()
            new_conference.abbreviation = extracted_conference['abbreviation'].upper()
            new_conference.name = extracted_conference['name']
            new_conference.league = new_league
            new_conference.save()
            
            extracted_divisions = extracted_conference['groups']
            for extracted_division in extracted_divisions:
                new_division = teams.models.Division()
                new_division.abbreviation = extracted_division['abbreviation'].upper()
                new_division.name = extracted_division['name']
                new_division.conference = new_conference
                new_division.save()
                
                division_id = extracted_division['groupId']
                espnUrl = "http://api.espn.com/v1/sports/" + sport_name + "/" + league_name + "/teams?group=" + str(division_id) + "&apikey=qvf4w5he6tszff4j3y3ugvus"
                
                contents, success = TeamDataRetriever.retrieve_json_contents(espnUrl)
                
                if success:
                    extracted_teams = contents['sports'][0]['leagues'][0]['teams']
                    for extracted_team in extracted_teams:
                        new_team = teams.models.Team()
                        new_team.abbreviation = extracted_team['abbreviation'].upper()
                        new_team.name = extracted_team['name']
                        new_team.location = extracted_team['location']
                        new_team.division = new_division
                        new_team.save()
                else:
                    print "failed to load divisions, read from: " + espnUrl
                    print "contents: " + str(contents)
                    return False
        print "-----------"
        return True