from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

# Create your models here.

# class GameUser(AbstractUser):

class Profile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='profile')
