#! coding: utf-8
from django.core.paginator import Paginator

from app.models import ProjectFile


class FileSearch(object):
    def __init__(self, query={}):

        self.dados = ProjectFile.objects

        self.project = query.get('project')

        if query.get('sord') == 'desc':
            self.order = '-%s' % query.get('sidx')
        else:
            self.order = query.get('sidx')

        self.page = query.get('page', 1)
        self.quant = query.get('rows', 10)

        self.registros = []

    def buscar(self):

        if self.project:
            self.dados = self.dados.filter(project=self.project)

        print(self.project)

        # Only active records
        # self.dados = self.dados.filter(active=True)
        return self.paginar()

    def paginar(self):

        paginator = Paginator(self.dados.order_by(self.order), self.quant)  # Show 25 contacts per page
        page_records = paginator.page(self.page)

        for registro in page_records:
            novo = {}
            novo['id'] = str(registro.id)
            novo['project'] = registro.project.id
            novo['created'] = registro.created.strftime('%d/%m/%Y')
            novo['status'] = registro.get_status_display()
            novo['log'] = registro.log
            novo['quantity'] = registro.quantity
            novo['start_exec'] = registro.start_exec.strftime(
                '%d/%m/%Y %H:%M:%S') if registro.start_exec else 'Não Iniciado'
            novo['end_exec'] = registro.end_exec.strftime(
                '%d/%m/%Y %H:%M:%S') if registro.end_exec else 'Não Finalizado'

            self.registros.append(novo)

        retorno = {}
        retorno['records'] = paginator.count
        retorno['page'] = self.page
        retorno['rows'] = self.registros
        retorno['total'] = paginator.num_pages

        return retorno



