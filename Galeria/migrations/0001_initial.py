# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('obraz', models.IntegerField()),
                ('comment', models.SlugField(max_length=1000)),
                ('date_created', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Obrazy',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('date_modified', models.DateField()),
                ('date_created', models.DateField()),
                ('image', models.ImageField(upload_to='photos')),
                ('album', models.IntegerField()),
                ('tags', models.TextField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
