from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from pydatagen import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^index.html$', 'app.views.index'),
    url(r'^conexao.html$', 'app.views.conexao'),
    ('^sobre(.html)?$', TemplateView.as_view(template_name='sobre.html')),
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
