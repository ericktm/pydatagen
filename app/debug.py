import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'pydatagen.settings'

import django

django.setup()

from app.cron import do

do()



