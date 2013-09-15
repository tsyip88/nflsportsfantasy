from django.conf.urls import patterns, url

from matchups import views

urlpatterns = patterns('',
    url(r'^submit', views.submit_picks_for_current_matchup, name='submit_picks'),
    url(r'^(?P<week_number>\d+)/submit', views.submit_picks_for_week, name='submit_picks_for_week'),
    url(r'^(?P<week_number>\d+)/(?P<user_id>\d+)/admin_submit', views.admin_submit_picks_for_week, name='admin_submit_picks_for_week'),
    url(r'^(\d+)/admin_scoreboard', views.admin_scoreboard_for_week, name='admin_scoreboard_for_week'),
    url(r'^$', views.scoreboard_current_week, name='scoreboard'),
    url(r'^(\d+)/scoreboard', views.scoreboard_for_week, name='scoreboard_for_week'),
    url(r'^matchup$', views.current_matchups, name='current_matchups'),
    url(r'^(\d+)/matchup', views.weekly_matchups, name='weekly_matchups'),
    url(r'^update_scores', views.update_current_scores, name='update_current_scores'),
    url(r'^(\d+)/update_scores', views.update_scores_for_week, name='update_scores_for_week'),
)
