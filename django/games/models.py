from django.conf import settings
from django.db import models
from django.core import validators

import datetime
from django.utils import timezone

import re

# Create your models here.
class Game(models.Model):
	creator            = models.ForeignKey(settings.AUTH_USER_MODEL)                    
	name               = models.CharField('Name of this Game', max_length=150)                                
	valid_email_suffix = models.CharField('Email Suffix', max_length=100,
		help_text='Whitelisted domain name',
		validators=[
			validators.RegexValidator(re.compile('^[\w.]+$'), 'Enter a valid email domain', 'invalid')
		]
	)

	created_at         = models.DateField('created_at')

	def save(self):
		if not self.id:
			if not self.created_at:
				self.created_at = timezone.now()

		super(Game, self).save()

	def __unicode__(self):
		return self.name