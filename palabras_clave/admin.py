from django.contrib import admin
from .models import PalabraClave
# Register your models here.

class PalabraClaveAdmin(admin.ModelAdmin):

	list_display = ('descripcion', 'cantidad_inscritos', )
	search_fields = ('descripcion', )

admin.site.register(PalabraClave,PalabraClaveAdmin)
