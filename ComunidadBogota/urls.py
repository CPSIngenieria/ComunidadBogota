from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'comunidades.views.ComunidadBogotaView', name='ComunidadBogotaView'),
    url(r'^busqueda/(?P<comunidad>[\w]+)/(?P<palabra_clave>[\w]+)/', 'comunidades.views.busqueda', name='busqueda'),

)

from django.conf import settings

# ... your normal urlpatterns here

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))