
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from wakkerdam.forms import CreateGameForm
from wakkerdam.functions import distribute_roles
from wakkerdam.models import Game
from wakkerdam.forms import JoinPlayerForm


def all_games(request):
	"""
		Shows all available Wakkerdam games...
	"""
	open_games = Game.objects.filter(state = 'join')
	return render(request, 'all_games.html', {
		'games': open_games,
	})


@require_GET # only for showing empty forms
def make_game(request):
	"""
		Show the empty form to the user who is starting a game.
	"""
	form = CreateGameForm(data = None)
	return render(request, 'make_game.html', {
		'form': form,
	})


def join_game(request):
	"""
		Show the empty form to the user who is starting a game.
	"""
	form = JoinPlayerForm(data = None)
	return render(request, 'join_game.html', {
		'form': form,
	})

@require_POST # only send completed forms here
def make_game_submit(request):
	"""
		Start a new game that people can join, using the provided form data.
	"""
	form = CreateGameForm(data = request.POST)
	if form.is_valid():
		""" save the new Game if it's valid """
		game = form.instance
		distribute_roles(game)
		form.save()
	return redirect(to = '%s?id=%d' % (reverse('wakkerdam_game'), game.id))


def show_game(request):
	try:
		id = int(request.GET['id'])
		game = Game.objects.get(id = id)
	except (KeyError, ValueError, Game.DoesNotExist), e: # if no id or not a valid id or no such game
		return redirect(to = '%s' % reverse('wakkerdam_game_not_found'))
	form = JoinPlayerForm(data = None)
	return render(request, 'show_game.html', {
		'game': game,
		'form': form,
	})


def game_not_found(request):
	return render(request, 'game_not_found.html')


