import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
import exrex

from app.core.generator.main import Generator
from app.models import Project


@login_required
def index(request, project=None):
    retorno = {}

    sql = ''

    project = Project.objects.get(pk=project)

    tables = project.app_table_project.filter(active=True).order_by('order').all()

    for table in tables:

        if table.insert:
            sql_insert = 'INSERT INTO %s (%s) VALUES (%s);\n'
            last_name = ''

            fabric = Generator()

            # get active fields
            fields = table.app_field_table.filter(active=True, insert=True).order_by('type').all()

            columns_names = ''
            for column in fields:
                if columns_names == '':
                    columns_names += '%s' % column.name
                else:
                    columns_names += ',%s' % column.name

            for i in range(table.quantity):
                values = ''
                for field in fields:
                    if field.options:
                        options = json.loads("""%s""" % field.options)
                    else:
                        options = dict()

                    value = 'teste'
                    # Case Integer
                    if field.type == 4:
                        if field.regex == '':
                            value = "%s" % fabric.get_regex('\d{2}')
                        else:
                            value = "%s" % fabric.get_regex(field.regex)
                    # case string
                    elif field.type == 1:
                        if field.regex == '':
                            value = "'%s'" % 'String'
                        else:
                            value = "'%s'" % exrex.getone(field.regex)
                    # Person Name
                    elif field.type == 2:
                        last_name = fabric.get_name().replace("\n", "")
                        value = "'%s'" % last_name
                    # Country name
                    elif field.type == 6:
                        value = "'%s'" % fabric.get_country()
                    # Case Foreign Key
                    elif field.type == 5:
                        value = "(SELECT %s FROM %s ORDER BY RANDOM() LIMIT 1)"
                        value = value % (field.to_field.name, field.to_field.table.name)
                    # Case Email address
                    elif field.type == 7:
                        if last_name == '':
                            value = "'%s'" % fabric.get_email(fabric.get_name())
                        else:
                            value = "'%s'" % fabric.get_email(last_name)
                    # Case Date
                    elif field.type == 3:
                        min = options.get('min', '01/01/1900')
                        max = options.get('max', '30/12/2050')

                        value = "'%s'" % fabric.get_date(min, max)

                    if values == '':
                        values += '%s' % value
                    else:
                        values += ', %s' % value

                # After generate all fields
                sql += sql_insert % (table.name, columns_names, values)

        else:
            print('Table not used')

    file = open('pydatagen/media/export.sql', 'w')
    file.write(sql)

    retorno['success'] = True
    retorno['message'] = 'Arquivo Gerado com sucesso!'

    return HttpResponse(json.dumps(retorno), content_type='text/json')