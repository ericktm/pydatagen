# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0005_remove_projectfile_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='insert',
        ),
        migrations.RemoveField(
            model_name='table',
            name='order',
        ),
        migrations.RemoveField(
            model_name='table',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='status',
            field=models.SmallIntegerField(default=4, choices=[(0, b'Agendado'), (1, b'Em execu\xc3\xa7\xc3\xa3o'),
                                                               (2, b'Conclu\xc3\xaddo'), (3, b'Processado com erros'),
                                                               (4, b'Rascunho')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tablefile',
            name='project_file',
            field=models.ForeignKey(editable=False, to='app.ProjectFile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tablefile',
            name='table',
            field=models.ForeignKey(verbose_name=b'Tabela', to='app.Table'),
            preserve_default=True,
        ),
    ]
