
from ruperton.models import Sorteo

def rupertones(request):
	sorteos = Sorteo.objects.all().order_by('-fecha_inicio_registro_compras')
	context = {
		'sorteos':sorteos,
	}