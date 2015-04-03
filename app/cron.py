#! coding:utf-8
import datetime
import json

import random
from django.utils import timezone

from app.core.generator.main import Generator
from app.models import ProjectFile, TableFile
from pydatagen.settings import SQL_DIR


def do():
    print('starting...')

    # project = Project.objects.get(pk=project)
    schedules = ProjectFile.objects.filter(status=0).all()

    for schedule in schedules:

        buffer_count = 0
        quant = 0
        updated_schedule = ProjectFile.objects.get(pk=schedule.id)
        w = Writter('%s.sql' % schedule.id)

        if updated_schedule.status == 0:
            schedule.status = 1
            schedule.start_exec = timezone.now()
            schedule.save()

            sql = ''

            for table in TableFile.objects.filter(project_file=updated_schedule, table__active=True).all():
                if table.quantity > 0:
                    sql_insert = 'INSERT INTO %s (%s) VALUES (%s);\n'
                    last_name = ''
                    fabric = Generator()
                    # get active fields
                    fields = table.table.app_field_table.filter(active=True, insert=True).order_by('type').all()
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

                                try:
                                    options = json.loads("""%s""" % options)
                                except Exception as e:
                                    schedule.status = 3
                                    schedule.log = 'Erro: %s ' % e.message
                                    schedule.save()

                            else:
                                options = dict()

                            value = 'initial'

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

                            elif field.type == 9:
                                value = "%s" % random.choice([True, False])

                            elif field.type == 10:
                                value = "'%s'" % fabric.get_bank()

                            if values == '':
                                values += '%s' % value
                            else:
                                values += ', %s' % value


                        # After generate all fields
                        sql += sql_insert % (table.table.name, columns_names, values)
                        buffer_count += 1
                        quant += 1

                        if buffer_count >= 500:
                            w.write(sql)
                            buffer_count = 0
                            sql = ''

                else:
                    schedule.log = 'Table not used'

            try:
                # if quant = 0, saves blank file
                w.write(sql)
                schedule.status = 2
                schedule.end_exec = timezone.now()
                schedule.log = 'Gerado com Sucesso!'
                schedule.quantity = quant
                schedule.save()

                # os.remove(path)
                print('SUCCESS')

                w.close()

            except Exception as e:
                schedule.status = 3
                schedule.log = 'Erro: %s ' % str(e)
                schedule.end_exec = datetime.datetime.now()
                schedule.save()
                print(e)


class Writter(object):
    def __init__(self, file_name='file.txt'):
        print('again')
        self.file = open('%s/%s' % (SQL_DIR, file_name), 'w+')

    def write(self, text='content'):
        self.file.write(text)

    def close(self):
        print('closing file..')
        self.file.close()
