from django.conf import settings

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url

from games.models import Game
from games.forms import GameCreateForm, GameDeleteForm

# Create your views here.

@login_required
def index(request):
	c = {} #Context
	c['games'] = Game.objects.filter(creator=request.user)
	return render(request, 'games/index.html', c,)

@login_required
def new(request, redirect_to="/games/"):
	c = {} #Context
	creation_form = GameCreateForm
	if request.method == "POST":
		form = creation_form(data=request.POST)
		if form.is_valid():

			# Ensure the user-originating redirection url is safe.
			redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

			# Okay, security check complete. Log the user in.
			# auth_login(request, form.get_user())
			game = form.save(commit=False);
			game.creator = request.user
			game.save()

			return HttpResponseRedirect(redirect_to)
	else:
		form = creation_form(None)

	c['form']  = form

	return render(request, 'games/new.html', c,)

@login_required
def edit(request, id_number):
	game = Game.objects.get(id=id_number)
	if (game == None):
		return HttpResponse(status=404)
	if (game.creator.id != request.user.id):
		return HttpResponse(status=403)

	c = {} #Context
	creation_form = GameCreateForm

	if request.method == "POST":
		form = creation_form(data=request.POST, instance=game)
		if form.is_valid():

			# Ensure the user-originating redirection url is safe.
			redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

			# Okay, security check complete. Log the user in.
			# auth_login(request, form.get_user())
			game = form.save(commit=False);
			game.creator = request.user
			game.save()

			return HttpResponseRedirect(redirect_to)
	else:
		form = creation_form(None, instance=game)

	c['game'] = game
	c['form'] = form

	return render(request, 'games/edit.html', c,)

@login_required
def delete(request, id_number):
	game = Game.objects.get(id=id_number)
	if (game == None):
		return HttpResponse(status=404)
	if (game.creator.id != request.user.id):
		return HttpResponse(status=403)

	c = {} #Context
	form = GameDeleteForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			if form.cleaned_data['confirm_delete'] == True:
				game.delete()
				return HttpResponseRedirect(resolve_url('games.views.index'))
	else:
		pass

	c['game'] = game
	c['form'] = form
	return render(request, 'games/delete.html', c,)