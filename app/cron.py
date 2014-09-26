#! coding:utf-8
import random
import datetime
import json

from django.core.files.base import File
import kronos

from app.core.generator.main import Generator
from app.models import ProjectFile


@kronos.register('*/1 * * * *')
def do():
    # project = Project.objects.get(pk=project)
    schedules = ProjectFile.objects.filter(status=0).all()

    for schedule in schedules:

        updated_schedule = ProjectFile.objects.get(pk=schedule.id)

        if updated_schedule.status == 0:
            schedule.status = 1
            schedule.save()

            project = schedule.project
            sql = ''
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
                                options = field.options.replace('\\', '\\\\')
                                options = json.loads("""%s""" % options)
                            else:
                                options = dict()

                            value = 'teste'
                            # Case Integer
                            if field.type == 4:
                                value = "%s" % fabric.get_regex(options.get('regex', '\d{2}'))

                            # case string
                            elif field.type == 1:
                                value = "'%s'" % fabric.get_regex(options.get('regex', 'String'))

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

                                provider = random.choice(options.get('providers', ['pydatagen.com']))
                                if last_name == '':
                                    value = "'%s'" % fabric.get_email(fabric.get_name(), provider)
                                else:
                                    value = "'%s'" % fabric.get_email(last_name, provider)
                            # Case Date
                            elif field.type == 3:
                                min = options.get('min', '01/01/1900')
                                max = options.get('max', '30/12/2050')

                                value = "'%s'" % fabric.get_date(min, max)

                            elif field.type == 8:
                                value = "'%s'" % fabric.get_login(last_name)

                            if values == '':
                                values += '%s' % value
                            else:
                                values += ', %s' % value

                        # After generate all fields
                        sql += sql_insert % (table.name, columns_names, values)

                else:
                    print('Table not used')

            try:
                file_name = '%s-%s.sql' % (project.id, datetime.datetime.now().strftime("%f"))

                file = open('pydatagen/media/tmp.sql', 'w+')
                file.write(sql)

                schedule.file.save(content=File(file),
                                   name=file_name)
                schedule.status = 2
                schedule.save()
            except Exception, e:
                schedule.status = 3
                schedule.save()
                print(e)
