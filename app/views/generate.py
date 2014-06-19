from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
import exrex
from faker.factory import Factory

from app.core.generator.main import Generator
from app.models import Project


@login_required
def index(request, project=None):
    retorno = []
    factory = Factory.create()

    quant = 1000
    sql = ''

    project = Project.objects.get(pk=project)

    tables = project.app_table_project.filter(active=True).all()

    for table in tables:

        sql_insert = 'INSERT INTO %s (%s) VALUES (%s);\n'

        fabric = Generator()

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
                        value = "%s" % fabric.get_regex('\d{2}')
                    else:
                        value = "%s" % fabric.get_regex(field.regex)
                #case string
                elif field.type == 1:
                    if field.regex == '':
                        value = "'%s'" % 'String'
                    else:
                        value = "'%s'" % exrex.getone(field.regex)
                #Person Name
                elif field.type == 2:
                    value = "'%s'" % fabric.get_name().replace("\n", "")

                if values == '':
                    values += '%s' % value
                else:
                    values += ', %s' % value
            #After generate all fields
            sql += sql_insert % (table.name, columns_names, values)

    file = open('pydatagen/output/export.sql', 'w')
    file.write(sql)

    return render_to_response('generate/index.html', {'retorno': retorno})