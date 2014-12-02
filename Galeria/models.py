from django.db import models


class obrazy(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=250)
    date_created = models.DateField()
    date_modified = models.DateField()
#    image = models.ImageField('Obraz', upload_to='photos', blank=True)
    album = models.IntegerField()



#class comments(models.Model):
#    user_id = models.OneToOneField(auth_user, id)
#    date_created = models.DateTimeField()
#    comment = models.SlugField(max_length=1000)
