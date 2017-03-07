from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Golfer(models.Model):
	firstname = models.CharField(max_length = 20)
	lastname = models.CharField(max_length = 20)
	user = models.OneToOneField(User, related_name='info', primary_key=True)
	picture = models.FileField(upload_to="images/golfer", blank=True)
	bio = models.CharField(max_length = 160)
	age = models.IntegerField()
	content_type = models.CharField(max_length=50)
	follows = models.ManyToManyField(User, related_name = 'followers')

class Course(models.Model):
	coursename = models.CharField(max_length = 30,primary_key=True)
	courserating = models.FloatField()
	picture = models.FileField(upload_to="images/course", blank=True)
	content_type = models.CharField(max_length=50)

class Hole(models.Model):
	# Course hole is a part of
	course = models.ForeignField(Course, default = None)

	# Hole information
	par = models.IntegerField()
	yardage = models.IntegerField()
	picture = models.FileField(upload_to="images/holes", blank=True)
	content_type = models.CharField(max_length=50)
	hole_number  = models.IntegerField()

	# Hole averages to rate difficulty of each hole
	scoreavg = models.FloatField()
	fwavg = models.FloatField()
	giravg = models.FloatField()
	puttavg = models.FloatField()

class GolfRound(models.Model):
	golfer = models.ForeignField(Golfer, default = None)
	course = models.ForeignField(Course, default = None)
	dateAdded = models.DateField(auto_now_add = True)
	lastEditDate = models.DateField(auto_now = True)
	# Final Score
	total_score = models.IntegerField()

	##Fairways stats
	total_fw_hit = models.IntegerField(default = 0)
	total_fw_miss = models.IntegerField(default = 0)

	#Fw miss stats
	fw_miss_left = models.IntegerField(default = 0)
	fw_miss_right = models.IntegerField(default = 0)
	

	##Green stats
	total_green_hit = models.IntegerField(defualt = 0)
	total_green_miss = models.IntegerField(defualt = 0)

	#Green Miss stats
	green_miss_short = models.IntegerField(default = 0)
	green_miss_left = models.IntegerField(default = 0)
	green_miss_right = models.IntegerField(default = 0)
	green_miss_long =  models.IntegerField(default = 0)

	#Green Hit stats
	green_hit_greater_30feet = models.IntegerField(default = 0)
	green_hit_greater_10feet = models.IntegerField(default = 0)
	green_hit_less_10feet = models.IntegerField(default = 0)

	##Putting stats
	total_putt = models.IntegerField(default = 0)

	#One putt stats
	one_putt_greater_30feet = models.IntegerField(default = 0)
	one_putt_greater_10feet = models.IntegerField(default = 0)
	one_putt_less_10feet = models.IntegerField(default = 0)

	#Two putt stats
	two_putt_greater_30feet = models.IntegerField(default = 0)
	two_putt_greater_10feet = models.IntegerField(default = 0)
	two_putt_less_10feet = models.IntegerField(default = 0)

	#Three putt stats
	three_putt_greater_30feet = models.IntegerField(default = 0)
	three_putt_greater_10feet = models.IntegerField(default = 0)
	three_putt_less_10feet = models.IntegerField(default = 0)

	###Scrmabling stats

	##Chipping stats
	chipping_made = models.IntegerField(deault = 0)
	chipping_missed = models.IntegerField(deault = 0)

	##Bunker stats
	bunker_made = models.IntegerField(deault = 0)
	bunker_missed = models.IntegerField(deault = 0)

	##Penalty stats
	total_penalty = models.IntegerField(default = 0)

	#Penalty type stats
	penalty_OB = models.IntegerField(default = 0)
	penalty_lost = models.IntegerField(default = 0)
	penalty_unplayable = models.IntegerField(default = 0)
	penalty_hazard = models.IntegerField(default = 0)
	penalty_other = models.IntegerField(default = 0)


class RoundHole(models.Model)
	golfer = models.ForeignField(Golfer, default = None)
	golfround = models.ForeignField(GolfRound, default = None)
	hole = models.ForeignField(Hole,default= None)
	
	# Round Notes
	notes = models.CharField(max_length = 160)

	#Score
	score = models.IntegerField()

	##Fairway
	fw_hit = models.BooleanField()
	fw_miss = models.BooleanField()

	#Fw miss stats
	fw_miss_left = models.BooleanField()
	fw_miss_right = models.BooleanField()
	

	##Green stats
	green_hit = models.BooleanField()
	green_miss = models.BooleanField()

	#Green Miss stats
	green_miss_short = models.BooleanField()
	green_miss_left = models.BooleanField()
	green_miss_right = models.BooleanField()
	green_miss_long =  models.BooleanField()

	#Green Hit stats
	green_hit_greater_30feet = models.BooleanField()
	green_hit_greater_10feet = models.BooleanField()
	green_hit_less_10feet = models.BooleanField()

	##Putting stats
	putts = models.IntegerField(default = 0)

	###Scrmabling stats

	##Chipping stats
	chipping_made = models.BooleanField()
	chipping_missed = models.BooleanField()

	##Bunker stats
	bunker_made = models.BooleanField()
	bunker_missed = models.BooleanField()

	##Penalty stats
	penalty = models.IntegerField(default = 0)

	#Penalty type stats
	penalty_OB = models.IntegerField(default = 0)
	penalty_lost = models.IntegerField(default = 0)
	penalty_unplayable = models.IntegerField(default = 0)
	penalty_hazard = models.IntegerField(default = 0)
	penalty_other = models.IntegerField(default = 0)

