from django.db import models


class obrazy(models.Model):
    id = models.AutoField()
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=250)
    date_created = models.DateField()
    date_modified = models.DateField()
    image = models.ImageField('Obraz', upload_to='photos', blank=True)
    album = models.IntegerField()

class auth_user(models.Model):
    id = models.AutoField()
    password = models.TextField(max_length=300)
    last_login = models.DateField()
    is_superuser = models.BooleanField()
    username = models.TextField(max_length=100)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=50)
    email = models.SlugField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateField()


class user_groups(models.Model):
    id = models.AutoField()
    user_id = models.OneToOneField(auth_user, id)
    group_id = models.IntegerField()


class auth_group(models.Model):
    id = models.AutoField()
    name = models.TextField()


class comments(models.Model):
    id = models.AutoField()
    user_id = models.OneToOneField(auth_user, id)
    date_created = models.DateTimeField()
    comment = models.SlugField(max_length=1000)
