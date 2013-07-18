from django.conf import settings

from django.db import models
from django.core import validators

import datetime
from django.utils import timezone

from django.core.urlresolvers import reverse

import re

# Create your models here.
class GameSession(models.Model):
	user      = models.ForeignKey(settings.AUTH_USER_MODEL)
	game      = models.ForeignKey('games.Game')

	killed    = models.BooleanField('Is User Killed', default=False)
	target    = models.ForeignKey('self', blank = True, null=True)
	num_kills = models.IntegerField('Kills', default = 0)
	kills     = models.ManyToManyField('self')

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