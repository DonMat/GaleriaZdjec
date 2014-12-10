# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0004_auto_20141210_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obrazy',
            name='date_modified',
        ),
    ]
