from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

import datetime

# Create your views here.
def index(request):
	return render_to_response('main/index.html', {})

def error404(request):
	return render_to_response('main/404.html', {})