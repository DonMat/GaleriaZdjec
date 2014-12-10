# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Galeria', '0002_gallerysettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='comments',
            name='obraz',
            field=models.ForeignKey(to='Galeria.Obrazy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='obrazy',
            name='album',
            field=models.ForeignKey(to='Galeria.Album'),
            preserve_default=True,
        ),
    ]
