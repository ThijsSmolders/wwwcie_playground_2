from django.core.urlresolvers import reverse
from django.http import request
from django.shortcuts import redirect, render
from forms import VotingFormDay
from models import Game, Player


def play_day(request):
	"Peter, jij vieze vuile teringproleet"
	try:
		id = int(request.GET['id'])
		game = Game.objects.get(id = id)
	except (KeyError, ValueError, Game.DoesNotExist), e: # if no id or not a valid id or no such game
		return redirect(to = '%s' % reverse('wakkerdam_game_not_found'))
	if game.state=='day':
		form = VotingFormDay(data = request.POST)
		return render(request, 'play_day.html', {
			'form': form,
			'game': game,
		})
		if form.is_valid():
			game.state = 'night'
			game.save()
	return redirect(to = '%s' % reverse('wakkerdam_waiting_room'))

def wait_for_votes(request):
	return render(request, 'waiting_room.html')

def play_night(request):
	""" Thijs is een motherfucker """

	try:
		id = int(request.GET['id'])
		game = Game.objects.get(id = id)
	except (KeyError, ValueError, Game.DoesNotExist), e: # if no id or not a valid id or no such game
		return redirect(to = '%s' % reverse('wakkerdam_game_not_found'))
	print Player.objects.filter(game = game, role = Player.WOLF)


