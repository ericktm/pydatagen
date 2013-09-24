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
        print "teste"

    def get_names(self):
        names = []
        arquivo = open('/home/ericktm/names.csv','r')
        for linha in arquivo:
            names.append(linha)

        return names


    def IntField(self, min=0, max=100):
        return random.randint(min, max)

    def DateField(self, start, end):
        start = datetime.datetime.strptime(start, '%d/%m/%Y').date()
        end = datetime.datetime.strptime(end, '%d/%m/%Y').date()
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())))

    '''
    Método responsável pela geração dos Nome de pessoas
    '''

    def NameField(self, gender=None):
        '''
        Os nomes são gerados conforme o gênero informado ao chamar o método
        Se o gênero não é informado, é gerado de qualquer gênero.
        '''
        name = ''

        if not gender:
            pass
        elif gender == 'M':
            name = 'João da Silva'
        elif gender == 'F':
            name = 'Mariana Rocha'

        name = choice(self.names)

        return name


    def EmailField(self, name="name sample"):
        #Caso seja informado o parâmero nome, o  mesmo será utilizado para geração do endereço de Email
        #Caso contrário, é gerado um Nome, que será convertido em endereço de Email
        if name:
            name = str(name)
            name = name.lower()
            name = re.sub(r"[ -]", ".", name)

        return name

if __name__ == '__main__':
    gen = Generator()
    print gen.IntField(min=400, max=9000)

    nome_gerado = gen.NameField()
    print nome_gerado
    email = gen.EmailField(nome_gerado)
    print email
    datain = datetime.datetime(2013, 12, 12)
    # datetime.datetime(1990,12,12),datetime.datetime(2013,12,30)
    # print gen.DateField('01/01/2000','30/12/2013')print gen.Name