# ! coding:utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('app.views',

                       url(r'^$', 'project.index'),
                       url(r'^project\.html$', 'project.index'),
                       url(r'^project/search\.html', 'project.search'),
                       url(r'^project/files/search\.html', 'project.file_search'),
                       url(r'^project/files/?(?P<id>\d*)?\.html', 'project.files'),
                       url(r'^project/files/delete/?(?P<id>\d*)?\.html', 'project.file_delete'),
                       url(r'^project/record/?(?P<id>\d*)?\.html', 'project.record'),
                       url(r'^project/delete/?(?P<id>\d*)?\.html', 'project.delete'),

                       url(r'^project/schedule/?(?P<id>\d*)?\.html', 'schedule.index'),
                       url(r'^schedule/search\.html', 'schedule.search'),
                       url(r'^schedule/delete/?(?P<id>\d*)?\.html', 'schedule.delete'),
                       url(r'^schedule/record/(?P<schedule_id>\d*)/(?P<id>\d*)?\.html', 'schedule.record'),
                       url(r'^schedule/finish/?(?P<id>\d*)?\.html', 'schedule.finish'),

                       url(r'^table/?(?P<project>\d*)?\.html', 'table.index'),
                       url(r'^table/search\.html', 'table.search'),
                       url(r'^table/record/(?P<project_id>\d+)/?(?P<id>\d*)?\.html', 'table.record'),
                       url(r'^table/delete/?(?P<id>\d*)?\.html', 'table.delete'),


                       url(r'^field/?(?P<table>\d*)?\.html', 'field.index'),
                       url(r'^field/search\.html', 'field.search'),
                       url(r'^field/record/(?P<table_id>\d+)/?(?P<id>\d*)?\.html', 'field.record'),
                       url(r'^field/delete/?(?P<id>\d*)?\.html', 'field.delete'),

                       url(r'^generate/(?P<project>\d*)\.html$', 'generate.index'),
                       url(r'^extrair\.html$', 'generate.extrair_nome'),
                       )