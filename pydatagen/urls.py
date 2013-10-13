from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from pydatagen import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^index.html$', 'app.views.index'),
                       url(r'^project$', 'app.views.projects'),
                       url(r'^project/record$', 'app.views.project'),
                       url(r'^project/record/(?P<id>\d+)$', 'app.views.project'),

                       url(r'^conexao.html$', 'app.views.conexao'),
                       url(r'^tables/(?P<id>\d+)', 'app.views.tables'),
                       url(r'^table/(?P<project_id>\d+)/(?P<id>\d+)?', 'app.views.table'),

                       url(r'^fields/(?P<id>\d+)$', 'app.views.fields'),
                       url(r'^field/(?P<table_id>\d+)/(?P<id>\d+)?', 'app.views.field'),
                       url(r'^field/associate$', 'app.views.associate'),
                       url(r'^delete(.html)?$', 'app.views.delete'),
                       url(r'^tabela/registro/?(?P<cod>\d*).html$', 'app.views.registro_tabela'),
                       url(r'^execution.html$', 'app.views.execution'),
                       ('^about(.html)?$', TemplateView.as_view(template_name='sobre.html')),
                       # Examples:
                       # url(r'^$', 'pydatagen.views.home', name='home'),
                       # url(r'^pydatagen/', include('pydatagen.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),

                       (r'^media/(.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
)
