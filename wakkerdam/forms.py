
from django.forms import ModelForm
from wakkerdam.models import Game, Player


class CreateGameForm(ModelForm):
	"""
		A form (digitaal formulier) that we 'complete' to change something about a game -
		in this case we create it (which is quite a change compared to not existing).
	"""
	class Meta:
		""" We want this form to change a Game """
		model = Game
		""" We only want the name field to be changed """
		fields = ['name',]

class JoinPlayerForm(ModelForm):

	class Meta:
		model = Player
		fields = ['name',]