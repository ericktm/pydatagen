from app.models import Project


class ProjectSearch(object):
    def __init__(self, query={}):
        self.id = query.get('id')
        self.nome = query.get('nome')

        self.dados = Project.objects

    def buscar(self):

        if self.id:
            self.dados.filter(pk=self.id)

        if self.nome:
            self.dados.filter(nome__icontains=self.nome)

        registros = []

        for registro in self.dados.all():
            novo = {}
            novo['id'] = registro.id
            novo['name'] = registro.name
            novo['created'] = registro.created.strftime('%d/%m/%Y')
            novo['edited'] = registro.edited.strftime('%d/%m/%Y') if registro.edited else ' - '
            registros.append(novo)

        print(registros)

        return {}



