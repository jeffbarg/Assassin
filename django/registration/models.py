from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create your models here.

class GameUser(AbstractUser):
	facebook_id = models.IntegerField('Facebook Numerical Id', blank=True)

class Profile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profile')
