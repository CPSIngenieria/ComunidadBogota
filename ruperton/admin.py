from django.contrib import admin
from .models import Sorteo, Concursante

class SorteoAdmin(admin.ModelAdmin):

	fieldsets = [
		('Informacion del sorteo', {'fields':['estado_sorteo']}),
		('Informacion fecha 1', 
			{'fields':
				['fecha_sorteo_1','premio_fecha_1','numero_ganador_1_fecha_1',
				'numero_ganador_2_fecha_1','numero_ganador_3_fecha_1','estado_fecha_1']
			}
		),
		('Informacion fecha 2', 
			{'fields':
				['fecha_sorteo_2','premio_fecha_2','numero_ganador_1_fecha_2',
				'numero_ganador_2_fecha_2','numero_ganador_3_fecha_2','estado_fecha_2']
			}
		),
		('Informacion fecha 3', 
			{'fields':
				['fecha_sorteo_3','premio_fecha_3','numero_ganador_1_fecha_3',
				'numero_ganador_2_fecha_3','numero_ganador_3_fecha_3','estado_fecha_3']
			}
		),
	]

	list_display = ('nombre_sorteo','fecha_creacion','estado_sorteo',)

class ConcursanteAdmin(admin.ModelAdmin):

	list_display = (
		'nombre','correo','direccion','telefono','establecimiento','acepto_terminos','sorteo',
	)

	search_fields = ['nombre','correo','establecimiento']

admin.site.register(Sorteo, SorteoAdmin)
admin.site.register(Concursante, ConcursanteAdmin)
