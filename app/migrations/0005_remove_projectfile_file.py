# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0004_auto_20150203_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectfile',
            name='file',
        ),
    ]
