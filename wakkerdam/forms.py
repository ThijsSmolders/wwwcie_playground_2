from django import forms
from django.forms import ModelForm, Form
from wakkerdam.models import Game, Player, WolfVote
from models import LynchVote


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

class NumberOfWolvesForm(Form):
	nr = forms.IntegerField(help_text='Aantal weerwolven in het spel')

class VotingFormDay(ModelForm):
	class Meta:
		""" We want this form to change a Game """
		model = LynchVote
		""" We only want the name field to be changed """
		fields = ['votee',]

class VotingFormWolves(ModelForm):
	class Meta:
		""" We want this form to change a Game """
		model = WolfVote
		""" We only want the name field to be changed """
		fields = ['wolfvotee',]