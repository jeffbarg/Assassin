"""
Form classes
"""

from django import forms

from games.models import Game

from django.contrib.admin.widgets import AdminDateWidget 
from django.utils import timezone

class GameCreateForm(forms.ModelForm):
	start_date = forms.DateTimeField(initial=timezone.now(), widget=forms.Textarea())

	class Meta:
		model = Game
		fields = ('name','valid_email_suffix','start_date')
        widgets = {
            'start_date':  AdminDateWidget,
        }

	def save(self, commit=True):
		game = super(GameCreateForm, self).save(commit=False)
		if commit:
			game.save()
		return game

class GameDeleteForm(forms.Form):
	confirm_delete = forms.BooleanField(required=False)