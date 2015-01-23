from django.conf.urls import patterns, url

from screen import views

urlpatterns = patterns('',
    url(r'^leagues$', views.leagues, name='leagues'),
    url(r'^leagueTeams/(?P<leagueID>\d+)$', views.leagueTeams, name='leagueTeams'),	
    url(r'^leagueCoaches/(?P<leagueID>\d+)$', views.leagueCoaches, name='leagueCoaches'),
    url(r'^teamPlayers/(?P<teamID>\d+)$', views.teamPlayers, name='teamPlayers'),
    url(r'^playerInfo/(?P<playerID>\d+)$', views.playerInfo, name='playerInfo'),


)
