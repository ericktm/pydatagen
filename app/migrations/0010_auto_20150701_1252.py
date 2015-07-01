# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_emailconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='type',
            field=models.IntegerField(max_length=2, choices=[(1, 'String'), (2, 'Nome de Pessoa'), (3, 'Data'), (4, 'Inteiro'), (5, 'Chave Estrangeira'), (6, 'País'), (7, 'Email'), (8, 'Username'), (9, 'Booleano'), (10, 'Bancos'), (11, 'Sequencial')], verbose_name='Tipo de Campo'),
        ),
    ]
