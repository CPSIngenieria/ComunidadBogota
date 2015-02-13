from django.contrib import admin
from .models import Sorteo, Concursante, Residente, Compra, Ganador

class ResidenteAdmin(admin.ModelAdmin):

	list_display = ('nombre', 'cedula', 'correo', 'direccion', 'telefono')

class CompraAdmin(admin.ModelAdmin):

	list_display = ('residente','monto','establecimiento','fecha_registro')

class SorteoAdmin(admin.ModelAdmin):

	fieldsets = [
		('Informacion del sorteo', 
			{'fields':
				['nombre','estado_sorteo','fecha_inicio_registro_compras','fecha_cierre_registro_compras']
			}
		),
		('Informacion fecha 1', 
			{'fields':
				['fecha_sorteo_1','premio_sorteo_1','numero_ganador_1_sorteo_1',
				'numero_ganador_2_sorteo_1','numero_ganador_3_sorteo_1','estado_sorteo_1',
				'ganador_sorteo_1']
			}
		),
		('Informacion fecha 2', 
			{'fields':
				['fecha_sorteo_2','premio_sorteo_2','numero_ganador_1_sorteo_2',
				'numero_ganador_2_sorteo_2','numero_ganador_3_sorteo_2','estado_sorteo_2',
				'ganador_sorteo_2']
			}
		),
		('Informacion premio por compras registradas', 
			{'fields':
				['premio_registro_compras','ganador_registro_compras']
			}
		),
	]

	list_display = (
		'nombre',
		'fecha_inicio_registro_compras',
		'estado_sorteo',
		'fecha_cierre_registro_compras'
		)

class ConcursanteAdmin(admin.ModelAdmin):

	list_display = (
		'nombre_concursante','correo_concursante','establecimiento','acepto_terminos','sorteo',
	)

	search_fields = ['nombre_concursante','correo_concursante','establecimiento']

class GanadorAdmin(admin.ModelAdmin):

	list_display = ('residente','foto_admin')

admin.site.register(Sorteo, SorteoAdmin)
admin.site.register(Concursante, ConcursanteAdmin)
admin.site.register(Residente, ResidenteAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Ganador, GanadorAdmin)