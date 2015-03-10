from django.core.paginator import Paginator

from app.models import Project


class ProjectSearch(object):
    def __init__(self, query={}):

        self.data = Project.objects

        self.id = query.get('id')
        self.name = query.get('name')

        if query.get('sord') == 'desc':
            self.order = '-%s' % query.get('sidx')
        else:
            self.order = query.get('sidx')

        self.page = query.get('page', 1)
        self.quant = query.get('rows', 10)

        self.records = []

    def seach(self):

        if self.id:
            self.data = self.data.filter(pk=self.id)

        if self.name:
            self.data = self.data.filter(name__icontains=self.name)

        # Only active records
        self.data = self.data.filter(active=True)
        return self.paginate()

    def paginate(self):

        paginator = Paginator(self.data.order_by(self.order), self.quant)  # Show 25 contacts per page
        page_records = paginator.page(self.page)

        for record in page_records:
            new_line = {'id': str(record.id),
                        'name': record.name,
                        'created': record.created.strftime('%d/%m/%Y'),
                        'quant': record.app_table_project.filter(active=True).count(),
                        'edited': record.edited.strftime('%d/%m/%Y') if record.edited else ' - '
            }
            self.records.append(new_line)

        return_data = {'records': paginator.count,
                       'page': self.page,
                       'rows': self.records,
                       'total': paginator.num_pages}

        return return_data



