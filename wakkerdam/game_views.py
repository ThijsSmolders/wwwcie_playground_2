from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from wakkerdam.models import Game, Player


def play_day(request):
	pass
def play_night(request):
	""" Thijs is een motherfucker """

	try:
		id = int(request.GET['id'])
		game = Game.objects.get(id = id)
	except (KeyError, ValueError, Game.DoesNotExist), e: # if no id or not a valid id or no such game
		return redirect(to = '%s' % reverse('wakkerdam_game_not_found'))
	print Player.objects.filter(game = game, role = Player.WOLF)


"""					request.user==game.initiator:
		game.state='start'
		game.save()
		form = NumberOfWolvesForm(data = None, initial={'nr':number_of_wolves(game.players.all().count())})
		return render(request, 'start_game.html', {
		'form': form,
		'game': game,
		})

	else:
		return redirect(to = '%s?id=%d' % (reverse('wakkerdam_game'), game.id)) """