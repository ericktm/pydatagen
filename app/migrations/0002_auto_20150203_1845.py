# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nome da Cidade')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nome do P\xc3\xa1is')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nome do Campo')),
                ('primary', models.BooleanField(default=False, verbose_name=b'Chave Prim\xc3\xa1ria')),
                ('null', models.BooleanField(default=False, verbose_name=b'Nulo')),
                ('type', models.IntegerField(max_length=2, verbose_name=b'Tipo de Campo',
                                             choices=[(1, b'String'), (2, b'Nome de Pessoa'), (3, b'Data'),
                                                      (4, b'Inteiro'), (5, b'Chave Estrangeira'), (6, b'Pa\xc3\xads'),
                                                      (7, b'Email'), (8, b'Username')])),
                ('insert', models.BooleanField(default=True, verbose_name=b'Popul\xc3\xa1vel')),
                ('size_max', models.IntegerField(null=True, verbose_name=b'Tamanho m\xc3\xa1ximo', blank=True)),
                ('options',
                 models.CharField(default=b'{}', max_length=500, null=True, verbose_name=b'Op\xc3\xa7\xc3\xb5es',
                                  blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nome do Projeto')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1000, verbose_name=b'Quantidade de registros')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to=b'project_files')),
                ('status', models.SmallIntegerField(default=0,
                                                    choices=[(0, b'Agendado'), (1, b'Em execu\xc3\xa7\xc3\xa3o'),
                                                             (2, b'Conclu\xc3\xaddo'), (3, b'Processado com erros')])),
                ('log', models.CharField(max_length=2000, blank=True)),
                ('start_exec', models.DateTimeField(null=True, blank=True)),
                ('end_exec', models.DateTimeField(null=True, blank=True)),
                ('project', models.ForeignKey(related_name='app_project_files_project', verbose_name=b'Projeto',
                                              to='app.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nome do Estado')),
                ('uf', models.CharField(max_length=2, verbose_name=b'Sigla')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True, editable=False)),
                ('country',
                 models.ForeignKey(related_name='app_state_country', verbose_name=b'P\xc3\xa1is', to='app.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nome da Tabela')),
                ('order', models.SmallIntegerField(verbose_name=b'Ordem')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True, editable=False)),
                ('insert', models.BooleanField(default=True, verbose_name=b'Popul\xc3\xa1vel')),
                ('quantity', models.IntegerField(default=1000, verbose_name=b'Quantidade de registros')),
                ('project',
                 models.ForeignKey(related_name='app_table_project', verbose_name=b'Projeto', to='app.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
            model_name='field',
            name='table',
            field=models.ForeignKey(related_name='app_field_table', verbose_name=b'Nome da Tabela', to='app.Table'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='field',
            name='to_field',
            field=models.ForeignKey(verbose_name=b'Campo Origem', blank=True, to='app.Field', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(related_name='app_city_state', verbose_name=b'Estado', to='app.State'),
            preserve_default=True,
        ),
    ]
