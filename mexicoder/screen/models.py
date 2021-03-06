from django.db import models

# Create your models here.

class Country(models.Model):
	name = models.CharField(max_length=30)
	flag = models.ImageField(upload_to='countryImages')

	def __str__(self):             
	        return self.name
	
class League(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	badge = models.ImageField(upload_to='leagueImages')
	creationDate = models.DateField('creation date')
	country = models.ForeignKey(Country)

	def __str__(self):             
	        return self.name


class Team(models.Model):
	name = models.CharField(max_length=50)
	badge = models.ImageField(upload_to='teamImages')
	creationDate = models.DateField('creation date')
	atackPoints = models.IntegerField(default = 0)
	defensePoints = models.IntegerField(default = 0)	
	country = models.ForeignKey(Country)
	league = models.ForeignKey(League)

	def __str__(self):             
	        return self.name


class Person(models.Model):
	name = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	dateBirth = models.DateField('date of birth')
	height = models.FloatField(default=0.0)
	weight = models.FloatField(default=0.0)
	imageProfile = models.ImageField(upload_to='profileImages')
	country = models.ForeignKey(Country)

	def __str__(self):             
	        return self.name


class Player(Person):
	LEFT = 'L'
    	RIGHT = 'R'
	FOOT_CHOICES = (
		(RIGHT, 'Right'),
		(LEFT, 'Left'),
	)
	shootingPoints = models.IntegerField(default=0)
	passingPoints = models.IntegerField(default=0)
	dribblingPoints = models.IntegerField(default=0)
	defendingPoints = models.IntegerField(default=0)
	headingPoints = models.IntegerField(default=0)
	position = models.CharField(max_length=20)
	foot = models.CharField(max_length=1,choices=FOOT_CHOICES,default=RIGHT)
	team = models.ForeignKey(Team)

class Coach(Person):
	victories= models.IntegerField(default=0)
	losses = models.IntegerField(default=0)
	directingPoints = models.IntegerField(default=0)
	team = models.OneToOneField(Team)
