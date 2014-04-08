#!- coding:utf-8
from django.db import models


TYPE_CHOICES = (
    (1, 'Lero Lero'),
    (2, 'Nome de Pessoa'),
    (3, 'Data'),
    (4, 'Inteiro'),
    (5, 'Chave Estrangeira')
)
#
#GENDER_CHOICES = (
#    (1, 'Masculino'),
#    (2, 'Feminino'),
#)

class Project(models.Model):
    name = models.CharField(verbose_name='Nome do Projeto', max_length=50)
    created = models.DateTimeField(auto_now=True, editable=False)
    edited = models.DateTimeField(null=True, editable=False)
    active = models.BooleanField(default=True, editable=False)

    def __unicode__(self):
        return self.name.upper()


class Table(models.Model):
    project = models.ForeignKey(verbose_name='Projeto', to=Project, related_name='app_table_project')
    name = models.CharField(verbose_name='Nome da Tabela', max_length=50)
    order = models.SmallIntegerField(verbose_name='Ordem')

    def __unicode__(self):
        return self.name


class Field(models.Model):
    table = models.ForeignKey(verbose_name='Nome da Tabela', to=Table, related_name='app_field_table')
    name = models.CharField(verbose_name='Nome do Campo', max_length=50)
    primary = models.BooleanField('Chave Primária', default=False, blank=False)
    null = models.BooleanField('Nulo', default=False)
    type = models.IntegerField(verbose_name='Tipo de Campo', max_length=2, choices=TYPE_CHOICES)
    insert = models.BooleanField(verbose_name='Populável', default=True)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.table)


class ForeignKey(models.Model):
    origin = models.ForeignKey(verbose_name='Campo Origem', to=Field, related_name='app_foreign_key_origin')
    destiny = models.ForeignKey(verbose_name='Campo Destino', to=Field, related_name='app_foreign_key_destiny')
