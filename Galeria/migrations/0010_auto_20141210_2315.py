# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0009_auto_20141210_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallerysettings',
            name='user',
        ),
        migrations.DeleteModel(
            name='GallerySettings',
        ),
    ]
