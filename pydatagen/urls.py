from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from pydatagen import settings

urlpatterns = patterns('',
                       url(r'^app/', include('app.urls')),
                       url(r'^(index.html)?$', TemplateView.as_view(template_name='layout.html')),
                       ('^about(.html)?$', TemplateView.as_view(template_name='sobre.html')),

                       (r'^media/(.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
)
