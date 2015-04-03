# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0007_auto_20150322_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(related_name='project_user', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
