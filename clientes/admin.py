from django.contrib import admin
from .models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):

	list_display = ('razon_social','direccion','comunidad','vista_logo_admin', )
	list_filter = ('comunidad', )
	search_fields = ('razon_social', )
	filter_horizontal = ('palabras_clave_inscritas', )


admin.site.register(Cliente,ClienteAdmin)