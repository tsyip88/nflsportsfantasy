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
        fmt = "%A, %b %d - %I:%M %p"
        return self.date_time.astimezone(pytz.timezone('US/Mountain')).strftime(fmt)
    
    def full_name(self):
        return self.date_time_string() + ' - ' + self.away_team.full_name() + ' at ' + self.home_team.full_name()
    
    def __unicode__(self): 
        return self.full_name()
    
    def winning_team(self):
        if self.home_team_score < 0 or self.away_team_score < 0 or self.away_team_score == self.home_team_score:
            return None
        if self.home_team_score > self.away_team_score:
            return self.home_team
        else:
            return self.away_team
    
class Pick(models.Model):
    matchup = models.ForeignKey(Matchup)
    selected_team = models.ForeignKey(Team)
    user = models.ForeignKey(User)
    
    def is_winning_pick(self):
        return self.matchup.winning_team() == self.selected_team
    
    def __unicode__(self): 
        return self.user.username + " - " + str(self.matchup.full_name())
    
class TieBreaker(models.Model):
    matchup = models.ForeignKey(Matchup)
    
    def __unicode__(self):
        return self.matchup.full_name()
    
class TieBreakerPick(models.Model):
    tie_breaker = models.ForeignKey(TieBreaker)
    predicted_total_score = models.SmallIntegerField()
    user = models.ForeignKey(User)
    
    def __unicode__(self): 
        return self.user.username + " - " + str(self.tie_breaker.matchup.full_name())