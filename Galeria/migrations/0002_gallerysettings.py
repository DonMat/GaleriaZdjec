# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GallerySettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
