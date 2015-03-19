#!- coding:utf-8
from django.db import models


TYPE_CHOICES = (
    (1, 'String'),
    (2, 'Nome de Pessoa'),
    (3, 'Data'),
    (4, 'Inteiro'),
    (5, 'Chave Estrangeira'),
    (6, 'País'),
    (7, 'Email'),
    (8, 'Username'),
    (9, 'Booleano'),
)

FILE_STATUS = (
    (0, 'Agendado'),
    (1, 'Em execução'),
    (2, 'Concluído'),
    (3, 'Processado com erros'),
    (4, 'Rascunho')
)


class Project(models.Model):
    name = models.CharField(verbose_name='Nome do Projeto', max_length=50)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(null=True, editable=False, auto_now=True)
    active = models.BooleanField(default=True, editable=False)

    def __unicode__(self):
        return self.name.upper()

    def __str__(self):
        return self.name.upper()


class ProjectFile(models.Model):
    project = models.ForeignKey(verbose_name='Projeto', to=Project, related_name='app_project_files_project')
    quantity = models.IntegerField(verbose_name='Quantidade de registros', default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    # file = models.
    status = models.SmallIntegerField(choices=FILE_STATUS, default=4)
    log = models.CharField(max_length=2000, blank=True)
    start_exec = models.DateTimeField(blank=True, null=True)
    end_exec = models.DateTimeField(blank=True, null=True)


class Table(models.Model):
    project = models.ForeignKey(verbose_name='Projeto', to=Project, related_name='app_table_project')
    name = models.CharField(verbose_name='Nome da Tabela', max_length=50)
    # order = models.SmallIntegerField(verbose_name='Ordem')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(null=True, editable=False, auto_now=True)
    active = models.BooleanField(default=True, editable=False)
    # insert = models.BooleanField(verbose_name='Populável', default=True)
    # quantity = models.IntegerField(verbose_name='Quantidade de registros', default=1000)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class TableFile(models.Model):
    project_file = models.ForeignKey(ProjectFile, editable=False)
    table = models.ForeignKey(Table, verbose_name='Tabela')
    order = models.SmallIntegerField(verbose_name='Ordem')
    quantity = models.IntegerField(verbose_name='Quantidade de registros', default=1000)

    def __unicode__(self):
        return self.table.name.upper()

    def __str__(self):
        return self.table.name.upper()


class Field(models.Model):
    table = models.ForeignKey(verbose_name='Nome da Tabela', to=Table, related_name='app_field_table')
    name = models.CharField(verbose_name='Nome do Campo', max_length=50)
    primary = models.BooleanField('Chave Primária', default=False, blank=False)
    null = models.BooleanField('Nulo', default=False)
    type = models.IntegerField(verbose_name='Tipo de Campo', max_length=2, choices=TYPE_CHOICES)
    insert = models.BooleanField(verbose_name='Populável', default=True)
    size_max = models.IntegerField(verbose_name='Tamanho máximo', null=True, blank=True)
    to_field = models.ForeignKey(verbose_name='Campo Origem', blank=True, null=True, to='self')
    options = models.CharField(verbose_name='Opções', max_length=500, null=True, blank=True, default="{}")
    # regex = models.CharField(verbose_name='Expressão regular', max_length=400, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(null=True, editable=False, auto_now=True)
    active = models.BooleanField(default=True, editable=False)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.table)

    def __str__(self):
        return '%s - %s' % (self.name, self.table)


class Country(models.Model):
    name = models.CharField(verbose_name='Nome do Páis', max_length=50)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(null=True, editable=False, auto_now=True)
    active = models.BooleanField(default=True, editable=False)


class State(models.Model):
    name = models.CharField(verbose_name='Nome do Estado', max_length=50)
    uf = models.CharField(verbose_name='Sigla', max_length=2)
    country = models.ForeignKey(verbose_name='Páis', to=Country, related_name='app_state_country')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(null=True, editable=False, auto_now=True)
    active = models.BooleanField(default=True, editable=False)


class City(models.Model):
    name = models.CharField(verbose_name='Nome da Cidade', max_length=50)
    state = models.ForeignKey(verbose_name='Estado', to=State, related_name='app_city_state')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(null=True, editable=False, auto_now=True)
    active = models.BooleanField(default=True, editable=False)


class FirstName(models.Model):
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=1)