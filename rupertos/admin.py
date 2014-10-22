from django.contrib import admin
from .models import Ruperto

# Register your models here.

class RupertoAdmin(admin.ModelAdmin):

	list_display = ('nombre','activo','vista_ruperto_admin',)
	list_filter = ('activo',)


admin.site.register(Ruperto,RupertoAdmin)