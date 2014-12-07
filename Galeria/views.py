from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from datetime import datetime
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


def albums_view(request):
    return render_to_response('albums.html')

def album_view(request, album_id):
    return render_to_response('album.html')

def image_view(request, album_id, image_id):
    return render_to_response('album.html')

def log_in(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/albums/')
    else:
        return render_to_response('log_in.html')

def register(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        return render_to_response('register.html')

def error403(request):
    return render_to_response('403.html')

def error404(request):
    return render_to_response('404.html')
