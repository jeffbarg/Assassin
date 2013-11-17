from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, QueryDict

import datetime

# Create your views here.
def index(request):
	user = request.user
	if (user != None and user.is_authenticated and user.is_active): 
		return HttpResponseRedirect(reverse('games:index'))
	c = {} #Context
	return render(request, 'main/homepage.html', c,)
	


def error404(request):
	return render_to_response('main/404.html', {})