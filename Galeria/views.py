from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.defaultfilters import title
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from Galeria.forms import *
from Galeria.models import *
from itertools import chain
from django.template import RequestContext
from django.shortcuts import render


def main_album(request, user_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    if request.user.id == int(user_id) or request.user.is_superuser:
        albums = Album.objects.filter(user_id=int(user_id))
        gallery = GallerySettings.objects.get(user_id=int(user_id))
        return render(request, "albums.html", {'albums' : albums, 'gallery': gallery})
    else:
        return render_to_response('404.html')

def main_album_edit(request, user_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    if request.user.id == int(user_id) or request.user.is_superuser:
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
    else:
        return render_to_response('404.html')



def sub_album_view(request, user_id, album_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')
    if request.user.id == int(user_id) or request.user.is_superuser:
        album = Album.objects.get(user_id=int(user_id), id=int(album_id))
        images = Obrazy.objects.filter(album_id=int(album_id))
        return render(request, 'album.html', {'album': album, 'images' : images, 'image_path': request.path})
    return render_to_response('404.html')

def sub_album_create(request, user_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')
    if request.user.id == int(user_id) or request.user.is_superuser:
        if request.method == 'POST':
            form = GalleryAlbumForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                album = Album(title=cd['title'], description=cd['description'])
                album.user_id = user_id
                album.save()
                return HttpResponseRedirect('/site/albums/' + user_id)
        else:
            form = GalleryAlbumForm()
        c = {}
        c.update(csrf(request))
        c['form'] = form
        return render(request, 'album_add.html', c)
    return render_to_response('404.html')

def sub_album_edit(request, user_id, album_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')
    if request.user.id == int(user_id) or request.user.is_superuser:
        if request.method == 'POST':
            form = GalleryAlbumForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                gallery = Album.objects.get(user_id=int(user_id), id=int(album_id))
                gallery.description = cd['description']
                gallery.title = cd['title']
                gallery.save()
                return HttpResponseRedirect('/site/albums/' + user_id + '/'+album_id)
            else:
                c = {}
                c.update(csrf(request))
                c['form'] = form
                return render(request, 'albums_edit.html', c)
        else:
            gallery = Album.objects.get(user_id=int(user_id), id=int(album_id))
            data = {'id': gallery.id, 'title': gallery.title, 'description': gallery.description}
            form = GalleryAlbumForm(initial=data)
            return render(request, 'albums_edit.html', {'form': form, 'del': True})
    return render_to_response('404.html')

def sub_album_delete(request, user_id, album_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')
    if request.user.id == int(user_id) or request.user.is_superuser:
        alb = Album.objects.get(user_id=int(user_id), id=int(album_id))
        if not None:
            alb.delete()
    return HttpResponseRedirect('/site/albums/'+user_id+'/')



def image_view(request, user_id, album_id, image_id):
    try:
        image = Obrazy.objects.get(id=int(image_id))
    except ObjectDoesNotExist:
        return render_to_response('404.html')

    comments = Comments.objects.filter(obraz_id=int(image_id))
    return render(request, 'image.html', {'image': image, 'comments': comments, 'owner':user_id})

def image_edit(request, user_id, album_id, image_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')
    if request.user.id == int(user_id) or request.user.is_superuser:
        image = Obrazy.objects.get(id=image_id)
        if request.method == 'POST':
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')
            tags = request.POST.get('tags', '')
            image.title = title
            image.description = description
            image.tags = tags
            image.save(update_fields=['title', 'description', 'tags'])
            return HttpResponseRedirect('/site/albums/'+user_id+'/'+album_id+'/'+image_id)
        else:
            data = {'id': image.id, 'title': image.title, 'description': image.description,
                    'tags': image.tags}
            form = UploadImageForm(initial=data)
            return render(request, 'image_edit.html', {'form': form})

    return render_to_response('404.html')

def image_delete(request, user_id, album_id, image_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')
    if request.user.id == int(user_id) or request.user.is_superuser:
        obraz = Obrazy.objects.get(album=int(album_id), id=int(image_id))
        if not None:
            obraz.delete()
            return HttpResponseRedirect('/site/albums/'+user_id+'/'+album_id)

    return render_to_response('404.html')

def image_upload(request, user_id, album_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')

    if request.user.id == int(user_id) or request.user.is_superuser:
        if request.method == 'POST':
            form = UploadImageForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                image = Obrazy(title=cd['title'],
                               description=cd['description'],
                               album_id=album_id,
                               date_created=datetime.now(),
                               image=cd['image'],
                               tags=cd['tags'])
                image.user_id = user_id
                image.save()
                return HttpResponseRedirect('/site/albums/'+user_id+'/'+album_id+'/')
        else:
            form = UploadImageForm()

        c = {}
        c.update(csrf(request))
        c['form'] = form
        return render(request, 'image_upload.html', c)
    return render_to_response('404.html')

def add_comment(request, user_id, album_id, image_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/site/log_in')
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            comment = Comments(comment=cd['comment'])
            comment.user = request.user
            comment.obraz = Obrazy.objects.get(id=image_id)
            comment.save()
            return image_view(request, user_id, album_id, image_id)
        else:
            form = CommentForm()

        c = {}
        c.update(csrf(request))
        c['form'] = form
        return render(request, 'image.html', c)


def search(request):
    q = request.GET.get('q')
    tags = q.split(' ')
    images = []
    for tag in tags:
        part_images = Obrazy.objects.filter(tags__contains=tag)
        images = list(chain(images,part_images))
    return render(request, "search.html", {'images': images, 'query': q})


def redirect_log_in(request):
    return HttpResponseRedirect('/site/log_in')

def auth_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/site/albums/' + str(request.user.id))

    if request.method == 'POST':
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=login, password=password)
        if user is not None:
            auth.login(request, user)
            ctx = RequestContext(request, {'user': user})
            return HttpResponseRedirect('/site/albums/' + str(user.id), ctx)
        else:
            return render(request, "log_in.html", {'message': "Nieprawidłowy login lub hasło"})
    return render(request, "log_in.html")

def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/site/log_in')

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/site/albums/' + str(request.user.id))

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/site/log_in/')
        else:
            c = {}
            c.update(csrf(request))
            c['form'] = form
            return render(request, 'register.html', c)
    else:
        c = {}
        c.update(csrf(request))
        c['form'] = RegisterForm()
        return render(request, 'register.html', c)



def error403(request):
    return render_to_response('403.html')

def error404(request):
    return render_to_response('404.html')

