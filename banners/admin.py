from django.contrib import admin
from .models import Banner

# Register your models here.

class BannerAdmin(admin.ModelAdmin):

	list_display = ('cliente', 'activo', 'fecha_vencimiento', 'vista_banner_admin', )
	list_filter = ('activo', )
	search_fields = ('cliente__razon_social', )
	raw_id_fields = ('cliente',)

admin.site.register(Banner, BannerAdmin)