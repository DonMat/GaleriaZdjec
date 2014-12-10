# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0008_gallerysettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerysettings',
            name='description',
            field=models.TextField(max_length=250, default=''),
            preserve_default=True,
        ),
    ]
