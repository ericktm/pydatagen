#!- coding:utf-8
from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField, IntegerField, SmallIntegerField
from django.db.models.fields.related import ForeignKey

TYPE_CHOICES = (
    ('STRING', 'Lero Lero'),
    ('NAME', 'Nome de Pessoa'),
    ('DATE', 'Data'),
    ('INT', 'Inteiro'),
    ('FORENGN', 'Chave Estrangeira')
)

GENDER_CHOICES = (
    (1, 'Masculino'),
    (2, 'Feminino'),
)

# Create your models here.
class Conection(Model):
    hostname = CharField(verbose_name="Endereço", max_length=50)
    username = CharField(verbose_name="Nome do Usuário", max_length=50)
    database = CharField(verbose_name="Nome do Banco de dados", max_length=50)
    password = CharField(verbose_name="Senha do Banco de dados", max_length=50, null=True, blank=True)
    # database = CharField(verbose_name = "Senha do Banco de dados", max_length = 50)
    created = DateTimeField("Created", auto_now=True, editable=False)

    def __unicode__(self):
        return self.hostname


class Table(Model):
    name = CharField(verbose_name="Nome da Tabela", max_length=50)
    created = DateTimeField("Criado em", auto_now=True, editable=False)
    database = ForeignKey(Conection, related_name="table_database_id")


class Type(Model):
    name = CharField(verbose_name="Nome do Tipo de Campo", max_length=50)


class Field(Model):
    name = CharField(verbose_name="Nome do Campo", max_length=50)
    field_type = ForeignKey(Type)
    size = IntegerField(verbose_name="Tamanho Máximo")
    created = DateTimeField("Criado em", auto_now=True, editable=False)
    table = ForeignKey(Table, related_name="field_table_id")


class Options(Model):
    pass


class FirstName(Model):
    value = CharField(verbose_name='Primeiro Nome', max_length=30)
    gender = SmallIntegerField(verbose_name='Gênero', max_length=1, choices=GENDER_CHOICES)


class LastName(Model):
    value = CharField(verbose_name='Sobrenome', max_length=30)

class City(Model):
    name = CharField(verbose_name='Nome da Cidade', max_length=40)

class State(Model):
    name = CharField(verbose_name='Nome do Estado', max_length=50)
    acronym = CharField(verbose_name='Sigla', max_length=2)

class Country(Model):
    name = CharField(verbose_name='Nome do País', max_length=50)