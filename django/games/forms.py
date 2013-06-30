"""
Form classes
"""

from django import forms
from games.models import Game

class GameCreateForm(forms.ModelForm):

	class Meta:
		model = Game
		fields = ('name','valid_email_suffix',)

	def save(self, commit=True):
		game = super(GameCreateForm, self).save(commit=False)
		if commit:
			game.save()
		return game

class GameDeleteForm(forms.Form):
	confirm_delete = forms.BooleanField(required=False)