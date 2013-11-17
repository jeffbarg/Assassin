"""
Form classes
"""

from django import forms

from games.models import Game

from django.contrib.admin.widgets import * 
from django.forms.extras.widgets import *

from datetimewidget.widgets import DateTimeWidget

from django.utils import timezone

class GameCreateForm(forms.ModelForm):
	start_date = forms.DateTimeField(initial=timezone.now(), widget=SelectDateWidget())

	class Meta:
		model = Game
		fields = ('start_date',)
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