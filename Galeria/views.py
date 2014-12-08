from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf

from datetime import datetime
from django.http import HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


def albums_view(request, user_id):
    t = loader.get_template("albums.html")
    c = Context({'user' : request.user})
    return HttpResponse(t.render(c))

def album_view(request, user_id, album_id):
    ctx = Context({'user': request.user})
    return render_to_response('album.html', ctx)

def image_view(request, user_id ,album_id, image_id):
    return render_to_response('album.html')

def log_in(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('log_in.html', c)

def register(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/')
    else:
        return render_to_response('register.html')

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
            ctx = Context(request, {'user': user})
            return HttpResponseRedirect('/site/albums/' + str(user.id), ctx)
        else:
            return HttpResponseRedirect('/site/log_in')
    return render_to_response('404.html')

def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/site/log_in')


def redirect_log_in(request):
    return HttpResponseRedirect('/site/log_in')