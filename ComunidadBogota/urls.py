from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^$', 'comunidades.views.ComunidadBogotaView', name='ComunidadBogotaView'),
    url(r'^ruperton/', 'ruperton.views.ruperton_home', name='ruperton_home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^busqueda/(?P<comunidad>[\w]+)/(?P<palabra_clave>[\w]+)/', 'comunidades.views.busqueda', name='busqueda'),
    url(r'^tips/', 'comunidades.views.tips', name='tip'),
)

from django.conf import settings

# ... your normal urlpatterns here

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))