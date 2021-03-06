#! coding: utf-8
from datetime import timedelta
import datetime

import os
import random
from random import choice
import re
import exrex

from pydatagen.settings import PROJECT_PATH


class Generator(object):
    def __init__(self):
        super(Generator, self).__init__()
        self.names = self.get_names()
        self.family_names = self.get_family_names()
        self.countries = self.get_countries()
        self.banks = self.get_banks()

    @staticmethod
    def get_names():
        names = []
        file_dir = os.path.join(PROJECT_PATH, 'res/')
        arquivo = open(file_dir + 'names.txt', 'r', encoding='UTF8')
        for linha in arquivo:
            names.append(linha.replace("'", "''"))
        return names

    @staticmethod
    def get_family_names():
        family_names = []
        file_dir = os.path.join(PROJECT_PATH, 'res/')
        arquivo = open(file_dir + 'family_names.txt', 'r', encoding='UTF8')
        for linha in arquivo:
            family_names.append(linha.replace("'", "''"))
        return family_names

    @staticmethod
    def get_banks():
        banks = []
        file_dir = os.path.join(PROJECT_PATH, 'res/')
        arquivo = open(file_dir + 'banks.txt', 'r', encoding='UTF8')
        for linha in arquivo:
            banks.append(linha.replace("'", "''"))
        return banks

    @staticmethod
    def get_countries():
        countries = []

        file_dir = os.path.join(PROJECT_PATH, 'res/')
        arquivo = open(file_dir + 'country_list.txt', 'r', encoding='UTF8')

        for line in arquivo:
            countries.append(line.replace('\n', '').replace("'", "''"))

        return countries

    def get_country(self):
        return random.choice(self.countries)

    def get_bank(self):
        return random.choice(self.banks)

    def get_int(self, min=0, max=100):
        """

        @param min:
        @param max:
        @return:
        """
        return random.randint(min, max)

    def get_date(self, start='01/01/1900', end='30/12/2000'):
        start = datetime.datetime.strptime(start, '%d/%m/%Y').date()
        end = datetime.datetime.strptime(end, '%d/%m/%Y').date()
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())))

    def get_regex(self, regex=str()):
        return exrex.getone(regex)


    '''
    Método responsável pela geração dos Nome de pessoas
    '''

    def get_name(self, gender=None):
        '''
        Os nomes são gerados conforme o gênero informado ao chamar o método
        Se o gênero não é informado, é gerado de qualquer gênero.
        '''
        return '%s %s' % (choice(self.names), choice(self.family_names))

    def get_login(self, name='name sample'):
        """
        Metodo utilizadopara geração de usernames
        @param name:
        @return:
        """
        if name:
            name = str(name)
            name = name.lower()
            name = re.sub(r"[ -]", ".", name)
            name = re.sub(r"[\t\b\n]", "", name)
            name = re.sub(r"\.{2}", "", name)
        return name

    def get_email(self, name="name sample", provider="pydatagen.com"):
        # Caso seja informado o parâmero nome, o  mesmo será utilizado para geração do endereço de Email
        # Caso contrário, é gerado um Nome, que será convertido em endereço de Email
        if name:
            name = str(name)
            name = name.lower()
            name = re.sub(r"[ -]", ".", name)
            name = re.sub(r"[\t\b\n]", "", name)
            name = re.sub(r"\.{2,}", "", name)
            name = '%s@%s' % (name, provider)
        return name


if __name__ == '__main__':
    gen = Generator()
    print(gen.get_int(min=400, max=9000))

    nome_gerado = gen.get_name()
    print(nome_gerado)
    email = gen.get_email(nome_gerado)
    print(email)
    datain = datetime.datetime(2013, 12, 12)

    # print gen.get_regex('')
    # datetime.datetime(1990,12,12),datetime.datetime(2013,12,30)
    # print gen.DateField('01/01/2000','30/12/2013')print gen.Name