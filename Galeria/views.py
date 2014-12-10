from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.defaultfilters import title
from Galeria.forms import *
from Galeria.models import *
from django.template import RequestContext
from django.shortcuts import render


def albums_view(request, user_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    albums = Album.objects.filter(user_id=int(user_id))
    gallery = GallerySettings.objects.get(user_id=int(user_id))
    return render(request, "albums.html", {'albums' : albums, 'gallery': gallery})


def main_album_edit(request, user_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    if request.method == 'POST':
        form = GallerySettingsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            gallery = GallerySettings.objects.get(user_id=int(user_id))
            gallery.description = cd['description']
            gallery.title=cd['title']
            gallery.save()
            return HttpResponseRedirect('/site/albums/' + str(request.user.id))
        else:
            c = {}
            c.update(csrf(request))
            c['form'] = form
            return render(request, 'albums_edit.html', c)
    else:
        gallery = GallerySettings.objects.get(user_id=int(user_id))
        data = {'id': gallery.id, 'title':gallery.title, 'description':gallery.description}
        form = GallerySettingsForm(initial=data)
        return render(request, 'albums_edit.html', {'form': form})


def sub_album_edit(request, user_id, album_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    if request.method == 'POST':
        form = GalleryAlbumForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            gallery = Album.objects.get(user_id=int(user_id), id=int(album_id))
            gallery.description = cd['description']
            gallery.title = cd['title']
            gallery.save()
            return HttpResponseRedirect('/site/albums/' + str(request.user.id) + '/'+album_id)
        else:
            c = {}
            c.update(csrf(request))
            c['form'] = form
            return render(request, 'albums_edit.html', c)
    else:
        gallery = Album.objects.get(user_id=int(user_id), id=int(album_id))
        data = {'id': gallery.id, 'title': gallery.title, 'description': gallery.description}
        form = GalleryAlbumForm(initial=data)
        return render(request, 'albums_edit.html', {'form': form})


def create_album(request, user_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    if request.method == 'POST':
        form = GalleryAlbumForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            album = Album(title=cd['title'], description=cd['description'])
            album.user_id = user_id
            album.save()
            return HttpResponseRedirect('/site/albums/' + str(user_id))
    else:
        form = GalleryAlbumForm()

    c = {}
    c.update(csrf(request))
    c['form'] = form
    return render(request, 'album_add.html', c)


def album_view(request, user_id, album_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    album = Album.objects.get(user_id=int(user_id), id=int(album_id))
    return render(request, 'album.html', {'albu': album})


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