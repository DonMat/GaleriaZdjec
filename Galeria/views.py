from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from Galeria.forms import RegisterForm

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

    c = {}
    c.update(csrf(request))
    return render_to_response('log_in.html', c)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/site/log_in/')

    c = {}
    c.update(csrf(request))
    c['form'] = RegisterForm()
    return render_to_response('register.html', c)


def error403(request):
    return render_to_response('403.html')


def error404(request):
    return render_to_response('404.html')


def auth_view(request):
    if request.method == 'POST':
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=login, password=password)
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/site/album/')
            response.set_cookie('user', user.username)
            request.session['user'] = user.username
            return response
        else:
            return HttpResponseRedirect('/site/log_in')
    return render_to_response('404.html')


def log_out(request):
    auth.logout(request)
    response = HttpResponseRedirect('/site/log_in')
    response.set_cookie('user', '')
    request.session['user'] = ''
    return response


def redirect_log_in(request):
     return HttpResponseRedirect('/site/log_in')