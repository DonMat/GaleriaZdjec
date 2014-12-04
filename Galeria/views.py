from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from datetime import datetime
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


def albums_view(request):
    return render_to_response('albums.html')
 
def log_in(request):
    return render_to_response('log_in.html')

def register(request):
    return render_to_response('register.html')