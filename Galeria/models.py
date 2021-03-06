from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Album(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, default='')

    def __str__(self):
        return self.title

class Obrazy(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos')
    tags = models.TextField(max_length=300)


class Comments(models.Model):
    user = models.ForeignKey(User)
    obraz = models.ForeignKey(Obrazy)
    comment = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now=True)


class GallerySettings(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, default='')



@receiver(pre_delete, sender=Obrazy)
def obrazy_delete(sender, instance, **kwargs):
    instance.image.delete(False)