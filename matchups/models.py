from teams.models import Team
from django.db import models
from django.contrib.auth.models import User
import pytz

class Matchup(models.Model):
    home_team = models.ForeignKey(Team, related_name="home_team")
    away_team = models.ForeignKey(Team, related_name="away_team")
    home_team_score = models.SmallIntegerField(default=-1)
    away_team_score = models.SmallIntegerField(default=-1)
    date_time = models.DateTimeField()
    
    def date_time_string(self):
        return str(self.date_time.astimezone(pytz.timezone('US/Mountain')))
    
    def full_name(self):
        return self.date_time_string() + ' - ' + self.away_team.full_name() + ' at ' + self.home_team.full_name()
    
    def __unicode__(self): 
        return self.full_name()
    
class Pick(models.Model):
    matchup = models.ForeignKey(Matchup)
    selected_team = models.ForeignKey(Team)
    user = models.ForeignKey(User)