# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0003_auto_20141210_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='user_id',
            new_name='user',
        ),
    ]
