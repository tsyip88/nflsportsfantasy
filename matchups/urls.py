from django.conf.urls import patterns, url

from matchups import views

urlpatterns = patterns('',
    url(r'^all_matchups', views.all_matchups, name='all_matchups'),
    url(r'^(\d+)/matchup', views.weekly_matchups, name='weekly_matchups'),
    url(r'^$', views.current_matchups, name='current_matchups'),
    url(r'^submit', views.submit_picks, name='submit_picks'),
    url(r'^all_results', views.all_results, name='all_results'),
)
