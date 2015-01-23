from django.shortcuts import render
from screen.models import *
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def leagues(request):
	data = serializers.serialize('json', League.objects.all())
	return HttpResponse(data, content_type='application/json')

def leagueTeams(request,leagueID):
	league=League.objects.get(pk=leagueID)
	data = serializers.serialize('json', league.team_set.all())
	return HttpResponse(data, content_type='application/json')

def leagueCoaches(request,leagueID):
	teams=League.objects.get(pk=leagueID).team_set.all()
	l=[]
	for t in teams:
		coach=t.coach
		l+=([Person.objects.get(pk=coach.person_ptr_id)]+[coach])
	data = serializers.serialize('json', l)
	return HttpResponse(data, content_type='application/json')

def teamPlayers(request,teamID):
	players=Team.objects.get(pk=teamID).player_set.all()
	l=[]
	for p in players:
		l+=[Person.objects.get(pk=p.person_ptr_id)]+[p]
	data = serializers.serialize('json', l)
	return HttpResponse(data, content_type='application/json')

def playerInfo(request,playerID):
	player=Player.objects.get(pk=playerID)
	data = serializers.serialize('json', [player])
	return HttpResponse(data, content_type='application/json')	
