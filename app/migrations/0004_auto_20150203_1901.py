# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0003_auto_20150203_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.SmallIntegerField(verbose_name=b'Ordem')),
                ('quantity', models.IntegerField(default=1000, verbose_name=b'Quantidade de registros')),
                ('project_file', models.ForeignKey(to='app.ProjectFile')),
                ('table', models.ForeignKey(to='app.Table')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectfile',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name=b'Quantidade de registros'),
            preserve_default=True,
        ),
    ]
