#!- coding:utf-8
from django.db import models


TYPE_CHOICES = (
    ('STRING', 'Lero Lero'),
    ('NAME', 'Nome de Pessoa'),
    ('DATE', 'Data'),
    ('INT', 'Inteiro'),
    ('FORENGN', 'Chave Estrangeira')
)
#
#GENDER_CHOICES = (
#    (1, 'Masculino'),
#    (2, 'Feminino'),
#)

class Project(models.Model):
    name = models.CharField(verbose_name='Nome do ')