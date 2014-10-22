from django.shortcuts import render
from django.http import HttpResponse

from clientes.models import Cliente
from palabras_clave.models import PalabraClave
from banners.models import Banner

from .models import Comunidad
import json

# Create your views here.

def ComunidadBogotaView(request):

	comunidades = Comunidad.objects.all()
	palabras_clave = PalabraClave.objects.all()
	banners = Banner.objects.filter( activo=True )[:3]
	argumentos = { 'comunidades':comunidades, 'palabras_clave':palabras_clave, 'banners':banners }

	# import ipdb; ipdb.set_trace()

	return render(request, 'comunidad_bogota.html', argumentos)

def busqueda(request, comunidad, palabra_clave):
	
	if comunidad == 'Cualquiera':
		matches = Cliente.objects.all()
	else:	
		matches = Cliente.objects.filter(comunidad__nombre=comunidad)

	filtro_clave = matches.filter(
		palabras_clave_inscritas__descripcion__icontains=palabra_clave
	)

	filtro_nombre = matches.filter(
		razon_social__icontains=palabra_clave
	)

	filtro_descripcion = matches.filter(
		descripcion__icontains=palabra_clave
	)

	resultado = list( set(filtro_clave) | set(filtro_nombre) | set(filtro_descripcion) )    #quita duplicados

	data = {
		'clientes': []
	}

	for c in resultado:
		data['clientes'].append({
			'razon_social':c.razon_social,
			'direccion':c.direccion,
			'descripcion':c.descripcion,
			'telefono':c.telefono,
			'celular':c.celular,
			'sitio_web':c.sitio_web,
			'logo':c.logo.url,
			'comunidad':c.comunidad.nombre,
			'enlace_facebook':c.enlace_facebook,
			'enlace_twitter':c.enlace_twitter,
			'enlace_youtube':c.enlace_youtube,
			'inicio_horario_atencion':c.inicio_horario_atencion.hour,
			'fin_horario_atencion':c.fin_horario_atencion.hour,
			})

	json_data = json.dumps(data)

	return HttpResponse(json_data, content_type='application/json')