#!- coding:utf-8
from httplib2 import CertificateHostnameMismatch
from django.db import models

TYPE_CHOICES = (
                ('STRING','Lero Lero'),
                ('NAME','Nome de Pessoa'),
                ('DATE','Data'),
                ('INT','Inteiro'),
                ('FORENGN','Chave Estrangeira')
                )

# Create your models here.
class Conection(models.Model):
    hostname = models.CharField(verbose_name = "Endereço", max_length = 50)
    username = models.CharField(verbose_name = "Nome do Usuário", max_length = 50)
    database = models.CharField(verbose_name = "Nome do Banco de dados", max_length = 50)
    # database = models.CharField(verbose_name = "Senha do Banco de dados", max_length = 50)
    created = models.DateTimeField("Created", auto_now = True, editable = False)

    def __unicode__(self):
        return self.hostname

class Table(models.Model):
    name = models.CharField(verbose_name = "Nome da Tabela", max_length = 50)
    created = models.DateTimeField("Criado em", auto_now = True, editable = False)
    database = models.ForeignKey(Conection, related_name = "table_database_id")

class Type(models.Model):
    name = models.CharField(verbose_name = "Nome do Tipo de Campo", max_length = 50)

class Field(models.Model):
    name = models.CharField(verbose_name = "Nome do Campo", max_length = 50)
    type = models.ForeignKey(Type)
    size = models.IntegerField(verbose_name = "Tamanho Máximo")
    created = models.DateTimeField("Criado em", auto_now = True, editable = False)
    table = models.ForeignKey(Table,related_name = "field_table_id")

class Options(models.Model):
    pass