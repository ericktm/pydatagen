#! coding: utf-8
import random
from datetime import timedelta
import datetime
from random import choice
import re


class Generator(object):
    def __init__(self):
        super(Generator, self).__init__()
        self.names = self.get_names()

    def get_names(self):
        names = []
        arquivo = open('names.csv', 'r')
        for linha in arquivo:
            names.append(linha)
        print len(names)
        return names

    def get_int(self, min=0, max=100):
        return random.randint(min, max)

    def get_date(self, start, end):
        start = datetime.datetime.strptime(start, '%d/%m/%Y').date()
        end = datetime.datetime.strptime(end, '%d/%m/%Y').date()
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())))

    def get_regex(self, regex=str()):
        result = rstr.xeger('\d{2}')
        print('teste')
        return rstr.xeger('\d{2}')


    '''
    Método responsável pela geração dos Nome de pessoas
    '''

    def get_name(self, gender=None):
        '''
        Os nomes são gerados conforme o gênero informado ao chamar o método
        Se o gênero não é informado, é gerado de qualquer gênero.
        '''
        return choice(self.names)


    def get_email(self, name="name sample"):
        #Caso seja informado o parâmero nome, o  mesmo será utilizado para geração do endereço de Email
        #Caso contrário, é gerado um Nome, que será convertido em endereço de Email
        if name:
            name = str(name)
            name = name.lower()
            name = re.sub(r"[ -]", ".", name)
            name = re.sub(r"[\t\b\n]", "", name)
            name = re.sub(r"\.{2,}", "", name)
            name = '%s@pydatagen.com' % name
        print name
        return name


if __name__ == '__main__':
    gen = Generator()
    print gen.get_int(min=400, max=9000)

    nome_gerado = gen.get_name()
    print nome_gerado
    email = gen.get_email(nome_gerado)
    print email
    datain = datetime.datetime(2013, 12, 12)

    #print gen.get_regex('')
    # datetime.datetime(1990,12,12),datetime.datetime(2013,12,30)
    # print gen.DateField('01/01/2000','30/12/2013')print gen.Name