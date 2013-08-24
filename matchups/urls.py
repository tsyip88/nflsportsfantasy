from django.conf.urls import patterns, url

from matchups import views

urlpatterns = patterns('',
    url(r'^submit', views.submit_picks_for_current_matchup, name='submit_picks'),
    url(r'^(\d+)/submit', views.submit_picks_for_week, name='submit_picks_for_week'),
    url(r'^$', views.scoreboard_current_week, name='scoreboard'),
    url(r'^(\d+)/scoreboard', views.scoreboard_for_week, name='scoreboard_for_week'),
    url(r'^matchup$', views.current_matchups, name='current_matchups'),
    url(r'^(\d+)/matchup', views.weekly_matchups, name='weekly_matchups'),
)
