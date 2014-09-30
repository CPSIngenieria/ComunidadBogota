from django.contrib import admin
from .models import Comunidad

# Register your models here.

class ComunidadAdmin(admin.ModelAdmin):

	list_display = ('nombre','cantidad_inscritos',)

admin.site.register(Comunidad,ComunidadAdmin)