# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0006_auto_20141210_2103'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GallerySettings',
        ),
    ]
