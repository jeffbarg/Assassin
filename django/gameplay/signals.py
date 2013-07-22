from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from gameplay.models import GameSession, GameEvent

## JB-TODO: make signup message a random message from a list of around 10

@receiver(post_save, sender=GameSession)
def create_signup_event(sender, **kwargs):
	session           = kwargs['instance']
	event             = GameEvent()
	
	event.game        = session.game
	event.from_user   = session
	event.message     = 'signed up to play.'
	event.action_type = 'S'

	event.save()
