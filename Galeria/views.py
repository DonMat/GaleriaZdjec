from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from Galeria.forms import *
from Galeria.models import *
from django.template import RequestContext
from django.shortcuts import render

def albums_view(request, user_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    albums = Album.objects.filter(user_id=int(user_id))
    return render(request, "albums.html", {'albums' : albums})


def albums_edit_view(request, user_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    if request.method == 'POST':
            return HttpResponseRedirect('/site/albums/' + str(request.user.id))

    albums = [
        {'title': 'tytuł 1',
         'description': 'opis 1',
         'id': '1'},
        {'title': 'tytuł 2',
         'description': 'opis 2',
         'id': '2'},
        {'title': 'tytuł 3',
         'description': 'opis 3',
         'id': '3'},
        {'title': 'tytuł 4',
         'description': 'opis 4',
         'id': '4'}
    ]

    form = {
        "title": "mój tytuł galerii",
        "description": "mój opis galerii"
    }

    # t = loader.get_template("albums_edit.html")
    # c = Context({'user': request.user, 'albums': albums, 'form': form})
    # return HttpResponse(t.render(c))
    return render(request, "albums_edit.html" ,{'albums': albums, 'form': form})


def album_view(request, user_id, album_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    ctx = RequestContext({'user': request.user})
    return render_to_response('album.html', ctx)


def image_view(request, user_id, album_id, image_id):
    return render_to_response('album.html')


def log_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/site/albums/' + str(request.user.id))

    return render(request, "log_in.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/site/log_in/')

    c = {}
    c.update(csrf(request))
    c['form'] = RegisterForm()
    return render(request, 'register.html', c)


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
            ctx = RequestContext(request, {'user': user})
            return HttpResponseRedirect('/site/albums/' + str(user.id), ctx)
        else:
            return HttpResponseRedirect('/site/log_in')
    return render_to_response('404.html')


def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/site/log_in')


def redirect_log_in(request):
    return HttpResponseRedirect('/site/log_in')


def upload_image(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/site/albums/1/')
    else:
        form = UploadImageForm()

    c = {}
    c.update(csrf(request))
    c['form'] = form
    return render(request, 'upload.html', c)