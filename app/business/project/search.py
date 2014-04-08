from django.core.paginator import Paginator
from app.models import Project


class ProjectSearch(object):
    def __init__(self, query={}):

        self.dados = Project.objects

        self.id = query.get('id')
        self.name = query.get('name')

        if query.get('sord') == 'desc':
            self.order = '-%s' % query.get('sidx')
        else:
            self.order = query.get('sidx')

        self.page = query.get('page', 1)
        self.quant = query.get('rows', 10)

        self.registros = []

    def buscar(self):

        if self.id:
            self.dados = self.dados.filter(pk=self.id)

        if self.name:
            self.dados = self.dados.filter(name__icontains=self.name)


        # Only active records
        self.dados = self.dados.filter(active=True)
        return self.paginar()

    def paginar(self):

        paginator = Paginator(self.dados.order_by(self.order), self.quant)  # Show 25 contacts per page
        page_records = paginator.page(self.page)

        for registro in page_records:
            novo = {}
            novo['id'] = str(registro.id)
            novo['name'] = registro.name
            novo['created'] = registro.created.strftime('%d/%m/%Y')
            novo['edited'] = registro.edited.strftime('%d/%m/%Y') if registro.edited else ' - '
            self.registros.append(novo)

        retorno = {}
        retorno['records'] = paginator.count
        retorno['page'] = self.page
        retorno['rows'] = self.registros
        retorno['total'] = paginator.num_pages

        return retorno



