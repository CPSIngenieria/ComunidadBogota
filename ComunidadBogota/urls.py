from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^$', 'comunidades.views.ComunidadBogotaView', name='ComunidadBogotaView'),

    url(r'^ruperton/$', 'ruperton.views.ruperton_home', name='ruperton_home'),
    url(r'^ruperton/acepta-terminos/$', 'ruperton.views.ruperton_acepta_terminos', name='ruperton_acepta_terminos'),
    url(r'^ruperton/compras/registro/$', 'ruperton.views.ruperton_compras_registro', name='ruperton_compras_registro'),
    url(r'^ruperton/terminos/(?P<correo_residente>[\w\W]+)/(?P<id_concursante>[\d]+)/$', 'ruperton.views.ruperton_terminos', name='ruperton_terminos'),
    url(r'^ruperton/compras/(?P<correo_residente>[\w\W]+)/$', 'ruperton.views.ruperton_compras', name='ruperton_compras'),
    
    url(r'^ruperton/(?P<correo_residente>[\w\W]+)/$', 'ruperton.views.ruperton_residente', name='ruperton_residente'),
    url(r'^login_view/$', 'ruperton.views.user_login', name='login_view'),
    url(r'^logout_view/$', 'ruperton.views.user_logout', name='logout_view'),
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