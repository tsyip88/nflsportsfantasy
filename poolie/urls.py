from django.conf.urls import patterns, include, url
from django.contrib import admin
from poolie import views
import django.contrib.auth.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poolie.views.home', name='home'),
    # url(r'^poolie/', include('poolie.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teams/', include('teams.urls', namespace="teams")),
    url(r'^matchups/', include('matchups.urls', namespace="matchups")),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^admin_actions/$', views.admin_actions, name='admin_actions'),
    url(r'^select_tie_breaker_matchups/$', views.select_tie_breaker_matchups, name='select_tie_breaker_matchups'),
    url(r'^$', views.index, name='index'),
    url(r'^user_options/$', views.user_options, name='user_options'),
    url(r'^change_password/$', django.contrib.auth.views.password_change, {'template_name':'change_password.html'}, name='password_change'),
    url(r'^password_changed/$', django.contrib.auth.views.password_change_done, {'template_name':'password_changed.html'}),
)
