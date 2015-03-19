#! coding:utf-8
from sqlalchemy import *

class Conection(object):
    """
    Classe responsável por efetuar a conexão com o banco de dados
    """
    def __init__(self, sgbd, server, user, password, database):
        super(Conection, self).__init__()
        strCon = str('mysql+mysqldb' + '://' + user + ':' + password + '@' + server + '/' + database)
        self.meta = MetaData(strCon)
        self.meta.reflect()
        print("Conectou ao banco de dados!")


    def listaTabelas(self):
        return self.meta.tables.keys()

    def listCampos(self,tabela):
        table = Table(str(tabela), self.meta)
        return table.columns

    def listAtributos(self,tabela,campo):
        table = Table(str(tabela), self.meta)
        return table.c[str(campo)]
