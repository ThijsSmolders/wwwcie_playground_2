from django.shortcuts import render
from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from forms import VotingFormDay, VotingFormWolves
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
	""" wopwopwop """

	try:
		id = int(request.GET['id'])
		game = Game.objects.get(id = id)
	except (KeyError, ValueError, Game.DoesNotExist), e: # if no id or not a valid id or no such game
		return redirect(to = '%s' % reverse('wakkerdam_game_not_found'))
	print Player.objects.filter(game = game, role = Player.WOLF)

	if Game.state == 'night'
		"""De weerwolven gaan stemmen"""
		player = Player.objects.filter(game = game, role = Player.WOLF, user = request.user)
		if len(player) == 1
			if player[0].alive:
				form = VotingFormWolves(data = request.POST)
				return render(request, 'play_night.html', {
			'form': form,
			'game': game,
		})
		if form.is_valid():
			game.state = 'day'
			game.save()
			else:
				return HttpResponse('Noob, je bent dood.')
		else:
			return HttpResponse('Je mag niet stemmen deze nacht. Alleen de coole wolven zijn uitgenodigd.')



