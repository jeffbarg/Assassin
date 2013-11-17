from django.conf import settings

from django.db import models
from django.core import validators

import datetime
from django.utils import timezone

from django.core.urlresolvers import reverse

import re

# Create your models here.

class GameSession(models.Model):
	user       = models.ForeignKey(settings.AUTH_USER_MODEL)
	game       = models.ForeignKey('games.Game')
	
	target     = models.OneToOneField('self', blank = True, null=True)
	killed     = models.BooleanField('Is User Killed', default=False)
	num_kills  = models.IntegerField('Kills', default = 0)
	
	created_at = models.DateTimeField('created_at')

	def save(self):
		if not self.id:
			if not self.created_at:
				self.created_at = timezone.now()

		super(GameSession, self).save()

	def __unicode__(self):
		return 'Game Session: ' + self.user.get_full_name()

	def get_absolute_url(self):
		return reverse('gameplay.views.index', args=[str(self.id)])

# Create your models here.
class GameEvent(models.Model):
	ACTION_TYPES = (
		('S', 'Sign Up'),
		('K', 'Kill'),
		('T', 'Text'),
	)

	game      = models.ForeignKey('games.Game')
	
	from_user = models.OneToOneField('gameplay.GameSession', blank = True, null=True, related_name='from_user')
	to_user = models.OneToOneField('gameplay.GameSession', blank = True, null=True, related_name='to_user')

	message = models.CharField(max_length=1000)
	action_type = models.CharField(max_length=1, choices=ACTION_TYPES) 

	created_at = models.DateTimeField('created_at')

	def save(self):
		if not self.id:
			if not self.created_at:
				self.created_at = timezone.now()

		super(GameEvent, self).save()

	def __unicode__(self):
		return 'Game Event: ' + self.message

