#! coding:utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
                       url(r'^$', 'project.index'),
                       url(r'^project\.html$', 'project.index'),
                       url(r'^project/search\.html', 'project.search'),
                       url(r'^project/record/?(?P<id>\d*)?\.html', 'project.record'),
)