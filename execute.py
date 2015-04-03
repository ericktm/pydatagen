import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'pydatagen.settings'
django.setup()

from app.cron import do
do()