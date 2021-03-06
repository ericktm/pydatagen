#! coding:utf-8
# from app.models import Conection
import json
import re
from sqlalchemy.schema import MetaData


class Mapper(object):

    def __init__(self, con = None, arquivo=None):

        # strCon = str('mysql+mysqldb' + '://' + con.username + ':' + con.password + '@' + con.hostname + '/' + con.database)
        -- strCon = str('mysql+mysqldb://root:ericktm@localhost/banco')
        self.meta = MetaData(strCon)
        print(self.meta.reflect())
        print("Conectou ao banco de dados!")
        
        if arquivo:
            #Implementar função para leitura e parser do arquivo json
            pass
        self.map = dict()


        # self.map['database'] = {
        #     'engine': sgbd,
        #     'server': servidor,
        #     'user': usuario,
        #     'password': senha,
        #     'database': banco
        # }

        self.map['tabelas'] = {}
        self.map['foreign_keys'] = dict()


    def conecta(self, sgbd, servidor, usuario, senha, banco):
        #self.con = Conection(sgbd, servidor, usuario, senha, banco)
        self.map['database'] = {
            'engine': sgbd,
            'server': servidor,
            'user': usuario,
            'password': senha,
            'database': banco
        }

        self.map['tabelas'] = {}
        self.map['foreign_keys'] = dict()

        self.getTables()
        # self.calcOrder()

    def addChild(self, chave, valor):
        self.map[chave] = valor

    def updateMapper(self, Conection):
        pass

    def getTables(self):
        print("processando tabelas")
        tabelas = self.con.listaTabelas()

        for tabela in tabelas:
            campos = self.con.listCampos(tabela)
            dcampos = {}
            for campo in campos:
                nome = str(campo.name)
                tipo = str(campo.type)
                nulo = str(campo.nullable)
                primario = str(campo.primary_key)
                chaves = campo.foreign_keys
                opcoes = self.getTipo(nome, tipo, primario, nulo)
                p_size = re.compile("\(\d*\)$")


                #Definir relacionamentos
                chaves = {}
                for chave in campo.foreign_keys:
                    self.addChaves(chave)
                if p_size.match(tipo):
                    print("possui tamanho")
                    # print vars(campo)
                # print 'Campo: %s - Tipo: %s - Chave Primaria: %s' % (nome, tipo, primario)
                dcampos[nome] = {
                    'tipo': tipo,
                    'primario': primario,
                    'nulo': nulo,
                    'opcoes': opcoes
                }

            #Adicionando relações da tabela ao mapeamento
            self.map['tabelas'][tabela] = dcampos

    def addChaves(self, chave):
        '''
        Método que adiciona as propriedades da foreign key ao mapeamento do banco
        '''

        tabela = str(chave.constraint.table)

        if not self.map['foreign_keys'].has_key(tabela):
            self.map['foreign_keys'][tabela] = {}

        k_tabela = str(chave.column.table)
        k_campo = str(chave.column.name)
        k_delete = str(chave.ondelete)
        k_update = str(chave.onupdate)
        k_constraint = str(chave.constraint.name)
        self.map['foreign_keys'][tabela][k_constraint] = {
            'tabela_referencia': k_tabela,
            'campo': k_campo,
            'delete': k_delete,
            'update': k_update
        }

    def getField(self):
        pass

    def getAtribute(self):
        pass

    def getTipo(self, nome, tipo, primario, nulo):
        """"
        Método responsável por reconhecer o tipo de dado a ser inserido no campo, baseando-se no nome da coluna
        e no tipo da dados aceito.
        """""
        opcoes = {}
        #Reconhecer o tipo de dado
        if re.match(r'.*(VARCHAR|TEXT).*', tipo):
            opcoes['inserir'] = 'lerolero'
            p_email = re.compile('email')
            p_address = re.compile("(logradouro|end(ereco)+)")
            p_phone = re.compile("(tele(fone)+|phone)")
            if re.match(r'(nome|name)', nome):
                opcoes['inserir'] = 'nome'
            elif p_email.match(nome):
                opcoes['inserir'] = 'email'
            elif p_address.match(nome):
                opcoes['inserir'] = 'endereco'
            elif p_phone.match(nome):
                opcoes['inserir'] = 'telefone'
                opcoes['mascara'] = "(99) 9999-9999"

        elif re.match(r'(INT|DECIMAL)', tipo):
            opcoes['inserir'] = 'inteiro'
            if primario == 'True':
                opcoes['inserir'] = 'primario'
            tamanho = re.match(r'(\d*)', tipo)
        elif re.match(r'(TIME|DATE)', tipo):
            opcoes['inserir'] = 'data'

        return opcoes

    def saveFile(self,filename):
        with open('../mapa.json', 'w') as outfile:
            json.dump(map.map, outfile)

    def saveTables(self):
        print("Salvando")

if __name__ == '__main__':
    map = Mapper()
    map.conecta('postgresql+psycopg2', 'localhost', 'pydatagen', 'py123gen', 'pydatagen')
    map.saveFile('arquivo.json')