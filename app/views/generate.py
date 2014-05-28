import re

from django.shortcuts import render_to_response
import exrex
from faker.factory import Factory

from app.models import Project


def index(request, project=None):
    retorno = []
    factory = Factory.create()

    quant = 1000
    sql = ''

    project = Project.objects.get(pk=project)

    tables = project.app_table_project.filter(active=True).all()

    for table in tables:

        sql_insert = 'INSERT INTO %s (%s) VALUES (%s);\n'

        #get active fields
        fields = table.app_field_table.filter(active=True, insert=True).all()

        columns_names = ''
        for column in fields:
            if columns_names == '':
                columns_names += '%s' % column.name
            else:
                columns_names += ',%s' % column.name

        for i in range(quant):
            values = ''
            for field in fields:
                value = 'teste'

                # Case Integer
                if field.type == 4:
                    if field.regex == '':
                        value = "%s" % exrex.getone('\d{2}')
                    else:
                        value = "%s" % exrex.getone(field.regex)
                #case string
                elif field.type == 1:
                    if field.regex == '':
                        value = "'%s'" % 'String'
                    else:
                        value = "'%s'" % exrex.getone(field.regex)
                #Person Name
                elif field.type == 2:
                    value = "'%s'" % re.escape(factory.name())

                if values == '':
                    values += '%s' % value
                else:
                    values += ', %s' % value
            #After generate all fields
            sql += sql_insert % (table.name, columns_names, values)

    file = open('export.sql', 'w')
    file.write(sql)

    return render_to_response('generate/index.html', {'retorno': retorno})