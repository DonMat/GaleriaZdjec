from django.db import models
from django.contrib.auth.models import User

class Obrazy(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=250)
    date_modified = models.DateField()
    date_created = models.DateField()
    image = models.ImageField(upload_to='photos')
    album = models.IntegerField()



class comments(models.Model):
    user = models.ForeignKey(User)
    obraz = models.IntegerField()
    comment = models.SlugField(max_length=1000)
    date_created = models.DateTimeField()
