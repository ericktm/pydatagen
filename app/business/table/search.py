from django.core.paginator import Paginator

from app.models import Table


class TableSearch(object):
    def __init__(self, query={}):

        self.data = Table.objects

        self.project = query.get('project', 0)
        self.id = query.get('id')
        self.name = query.get('name')

        if query.get('sord') == 'desc':
            self.order = '-%s' % query.get('sidx')
        else:
            self.order = query.get('sidx')

        self.page = query.get('page', 1)
        self.quant = query.get('rows', 10)

        self.registros = []

    def search(self):

        if self.id:
            self.data = self.data.filter(pk=self.id)

        if self.name:
            self.data = self.data.filter(name__icontains=self.name)

        if self.project:
            self.data = self.data.filter(project=self.project)

        # Only active records
        #self.data = self.data.filter(active=True)
        print('Table search: %s' % self.data.query)
        return self.paginate()

    def paginate(self):

        paginator = Paginator(self.data.order_by(self.order), self.quant)  # Show 25 contacts per page
        page_records = paginator.page(self.page)

        for registro in page_records:
            new = {'id': str(registro.id),
                   'name': registro.name,
                   'order': registro.order,
                   'created': registro.created.strftime('%d/%m/%Y'),
                   'edited': registro.edited.strftime('%d/%m/%Y') if registro.edited else ' - '
            }
            self.registros.append(new)

        return_data = {'records': paginator.count,
                       'page': self.page,
                       'rows': self.registros,
                       'total': paginator.num_pages
        }

        return return_data



