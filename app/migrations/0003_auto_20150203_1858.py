# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0002_auto_20150203_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablefile',
            name='project_file',
        ),
        migrations.RemoveField(
            model_name='tablefile',
            name='table',
        ),
        migrations.DeleteModel(
            name='TableFile',
        ),
        migrations.RemoveField(
            model_name='projectfile',
            name='quantity',
        ),
    ]
