# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Galeria', '0005_remove_obrazy_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obrazy',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
