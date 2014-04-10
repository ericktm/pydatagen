#! coding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
                       url(r'^$', 'project.index'),
                       url(r'^project\.html$', 'project.index'),
                       url(r'^project/search\.html', 'project.search'),
                       url(r'^project/record/?(?P<id>\d*)?\.html', 'project.record'),
                       url(r'^project/delete/?(?P<id>\d*)?\.html', 'project.delete'),


                       url(r'^table/?(?P<project>\d*)?\.html', 'table.index'),
                       url(r'^table/search\.html', 'table.search'),
                       url(r'^table/record/(?P<project_id>\d+)/?(?P<id>\d*)?\.html', 'table.record'),

                       url(r'^generate\.html$', 'generate.index'),
)