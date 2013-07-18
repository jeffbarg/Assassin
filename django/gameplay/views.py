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

@login_required
def index(request, id_number):	
	c = {} #Context

	game = Game.objects.get(id=id_number)
	c['game'] = game
	
	if (game == None):
		return HttpResponse(status=404)

	sessions_query = request.user.gamesession_set.filter(game=game)
	if (sessions_query.count() == 0):
		return HttpResponseRedirect(reverse('game-request-invite', args=(game.id,)))

	now = timezone.now()
	if (game.start_date < now):
		return HttpResponse('TODO: add registered screen');
	else:
		return render(request, 'gameplay/index.html', c,)

@login_required
def request_invite(request, id_number):
	c = {} #Context

	game = Game.objects.get(id=id_number)
	c['game'] = game
	
	if (game == None):
		return HttpResponse(status=404)

	now = timezone.now()
	if (game.start_date > now):
		return HttpResponse('TODO: add game already started screen');

	if request.method == "GET":
		sessions_query = request.user.gamesession_set.filter(game=game)
		if (sessions_query.count() != 0):
			return HttpResponseRedirect(reverse('game-index', args=(game.id,)));
		
		return render(request, 'gameplay/request_invite.html', c,)	
	else:
		# Perform check to see if user is allowed to join game
		user = request.user
		if (game.allows_user(user)):
			game.register_user(user)
			return HttpResponseRedirect(reverse('game-index', args=(game.id,)))
