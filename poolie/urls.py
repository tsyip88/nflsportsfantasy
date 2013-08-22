from django.conf.urls import patterns, include, url
from django.contrib import admin
from poolie import views
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
    url(r'^$', views.index, name='index'),
)
