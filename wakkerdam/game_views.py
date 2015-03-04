
from audioop import reverse
from django.shortcuts import redirect
from forms import VotingFormDay
from models import Game, Player


def play_day(request):
	try:
		id = int(request.GET['id'])
		game = Game.objects.get(id = id)
	except (KeyError, ValueError, Game.DoesNotExist), e: # if no id or not a valid id or no such game
		return redirect(to = '%s' % reverse('wakkerdam_game_not_found'))
	if game.state=='day':
		form = VotingFormDay(data = request.POST)
		if form.is_valid():
			game.state = 'night'
			game.save()
	return redirect(to = '%s?id=%d' % (reverse('wakkerdam_night'), game.id))

def play_night(request):
	""" Thijs is een motherfucker """

	try:
		id = int(request.GET['id'])
		game = Game.objects.get(id = id)
	except (KeyError, ValueError, Game.DoesNotExist), e: # if no id or not a valid id or no such game
		return redirect(to = '%s' % reverse('wakkerdam_game_not_found'))
	print Player.objects.filter(game = game, role = Player.WOLF)


