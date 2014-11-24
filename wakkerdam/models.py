
from django.db import models


class Game(models.Model):
	"""
		Represent a play session of Wakkerdam
	"""
	name = models.CharField(max_length = 32)
	state = models.CharField(max_length = 10, choices = (
		('join', 'Players are joining'),
		('start', 'The game is starting'),
		('day', 'Playing; it is day in the game'),
		('night', 'Playing; it is night in the game'),
		('over', 'The game has been completed!'),
	), default = 'join')
	started = models.DateTimeField(auto_now_add = True)


