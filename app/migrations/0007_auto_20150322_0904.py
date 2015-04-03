# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20150212_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=1, related_name='project_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(verbose_name='Nome da Cidade', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(verbose_name='Estado', related_name='app_city_state', to='app.State'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(verbose_name='Nome do Páis', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='insert',
            field=models.BooleanField(verbose_name='Populável', default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(verbose_name='Nome do Campo', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='null',
            field=models.BooleanField(verbose_name='Nulo', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='options',
            field=models.CharField(blank=True, verbose_name='Opções', null=True, default='{}', max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='primary',
            field=models.BooleanField(verbose_name='Chave Primária', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='size_max',
            field=models.IntegerField(verbose_name='Tamanho máximo', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='table',
            field=models.ForeignKey(verbose_name='Nome da Tabela', related_name='app_field_table', to='app.Table'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='to_field',
            field=models.ForeignKey(verbose_name='Campo Origem', blank=True, null=True, to='app.Field'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='field',
            name='type',
            field=models.IntegerField(verbose_name='Tipo de Campo',
                                      choices=[(1, 'String'), (2, 'Nome de Pessoa'), (3, 'Data'), (4, 'Inteiro'),
                                               (5, 'Chave Estrangeira'), (6, 'País'), (7, 'Email'), (8, 'Username'),
                                               (9, 'Booleano'), (10, 'Bancos')], max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(db_index=True, default=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(verbose_name='Nome do Projeto', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='project',
            field=models.ForeignKey(verbose_name='Projeto', related_name='app_project_files_project', to='app.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantidade de registros', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='status',
            field=models.SmallIntegerField(db_index=True, default=4,
                                           choices=[(0, 'Agendado'), (1, 'Em execução'), (2, 'Concluído'),
                                                    (3, 'Processado com erros'), (4, 'Rascunho')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(verbose_name='Páis', related_name='app_state_country', to='app.Country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(verbose_name='Nome do Estado', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='state',
            name='uf',
            field=models.CharField(verbose_name='Sigla', max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table',
            name='active',
            field=models.BooleanField(db_index=True, default=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(verbose_name='Nome da Tabela', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table',
            name='project',
            field=models.ForeignKey(verbose_name='Projeto', related_name='app_table_project', to='app.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tablefile',
            name='order',
            field=models.SmallIntegerField(verbose_name='Ordem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tablefile',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantidade de registros', default=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tablefile',
            name='table',
            field=models.ForeignKey(verbose_name='Tabela', to='app.Table'),
            preserve_default=True,
        ),
    ]
