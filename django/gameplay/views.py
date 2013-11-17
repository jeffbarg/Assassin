from django.conf import settings

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url

from django.utils import timezone

# Create your views here.
from games.models import Game
from gameplay.models import GameSession


def index(request, id_number):
	game = Game.objects.get(id=id_number)
	
	if (game == None):
		return HttpResponse(status=404)

	user = request.user
	now = timezone.now()

	game_user_sessions =  user.gamesession_set.filter(game=game) if (user and user.is_authenticated and user.is_active) else None

	is_game_member = game_user_sessions != None and game_user_sessions.count() != 0
	is_game_started = game.start_date < now

	if (not is_game_member and not is_game_started):
		return HttpResponseRedirect(reverse('gameplay:invite', args=(game.id,)))

	# Now execute Gameplay logic
	c = {} #Context
	
	c['game']           = game
	c['user_sessions']  = game_user_sessions
	
	c['is_game_member'] = is_game_member
	c['game_started']   = is_game_started
	
	c['single_col']     = (is_game_member and not is_game_started)
	return render(request, 'gameplay/index.html', c,)

@login_required
def request_invite(request, id_number):
	c = {} #Context

	game = Game.objects.get(id=id_number)
	c['game'] = game
	
	if (game == None):
		return HttpResponse(status=404)

	if request.method == "GET":
		sessions_query = request.user.gamesession_set.filter(game=game)
		if (sessions_query.count() != 0):
			return HttpResponseRedirect(reverse('gameplay:index', args=(game.id,)));
		
		return render(request, 'gameplay/request_invite.html', c,)	
	else:
		# Perform check to see if user is allowed to join game
		user = request.user
		if (game.allows_user(user)):
			game.register_user(user)
			return HttpResponseRedirect(reverse('gameplay:index', args=(game.id,)))
		else:
			c['error_message'] = 'You are not permitted to join this game.'
			return render(request, 'gameplay/request_invite.html', c,) 
