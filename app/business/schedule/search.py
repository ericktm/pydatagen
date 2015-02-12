#! coding: utf-8
from django.core.paginator import Paginator

from app.models import TableFile


class ScheduleSearch(object):
    def __init__(self, query={}):

        self.dados = TableFile.objects

        self.table = query.get('table')
        self.project = query.get('project')
        self.schedule = query.get('schedule')

        if query.get('sord') == 'desc':
            self.order = '-%s' % query.get('sidx')
        else:
            self.order = query.get('sidx')

        self.page = query.get('page', 1)
        self.quant = query.get('rows', 10)

        self.registros = []

    def buscar(self):

        if self.table:
            self.dados = self.dados.filter(table=self.table)

        if self.schedule:
            self.dados = self.dados.filter(project_file=self.schedule)

        print('TableFile search: %s' % self.dados.query)
        return self.paginar()

    def paginar(self):

        paginator = Paginator(self.dados.order_by(self.order), self.quant)  # Show 25 contacts per page
        page_records = paginator.page(self.page)

        for registro in page_records:
            novo = {}
            novo['id'] = str(registro.id)
            novo['table'] = registro.table.name
            novo['table_id'] = registro.table.id
            novo['order'] = registro.order
            novo['quantity'] = registro.quantity
            self.registros.append(novo)

        retorno = {}
        retorno['records'] = paginator.count
        retorno['page'] = self.page
        retorno['rows'] = self.registros
        retorno['total'] = paginator.num_pages

        return retorno



