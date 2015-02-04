import mandrill
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from ruperton.models import Concursante, Sorteo

def ruperton_home(request):
	return render(request, 'ruperton/ruperton_home.html')

def ruperton_sorteo(request, id_sorteo):
	return render(request, 'ruperton/ruperton_home.html')

def ruperton_terminos(request, id_concursante):

	concursante = get_object_or_404(Concursante, pk=id_concursante)
	id_sorteo = concursante.sorteo.id
	sorteo = get_object_or_404(Sorteo, pk=id_sorteo)

	if sorteo.estado_sorteo == 'CE':
		return render(request, 'ruperton/terminos_vencidos.html')
	if concursante.acepto_terminos:
		return render(request, 'ruperton/terminos_aceptados.html')
	else:
		context = {
			'nombre_concursante':concursante.nombre,
			'id_sorteo':id_sorteo,
			'id_concursante':id_concursante,
		}
		return render(request, 'ruperton/terminos.html', context)

def ruperton_acepta_terminos(request):

	id_sorteo = request.POST['id_sorteo']
	id_concursante = request.POST['id_concursante']

	# Verificamos que el sorteo este en inscripciones:
	sorteo = get_object_or_404(Sorteo, pk=id_sorteo)
	concursante = Concursante.objects.get(pk=id_concursante)

	if sorteo.estado_sorteo == 'IN':
		if not concursante.acepto_terminos:	
			concursante.acepto_terminos = True
			concursante.save()

			# Buscamos las personas con esos numeros y les envimos un correo:
			numero_ganador_1 = concursante.numero_ganador_1
			numero_ganador_2 = concursante.numero_ganador_2
			numero_ganador_3 = concursante.numero_ganador_3

			listado_concursantes_mismos_numeros = Concursante.objects.filter(
				numero_ganador_1=numero_ganador_1,
				numero_ganador_2=numero_ganador_2,
				numero_ganador_3=numero_ganador_3,
			)

			cantidad_participantes = listado_concursantes_mismos_numeros.count()

			for concursante_repetido in listado_concursantes_mismos_numeros:
				nombre_concursante = concursante_repetido.nombre
				email_concursante = concursante_repetido.correo

				try:
					mandrill_client = mandrill.Mandrill('_SoGpYeWNJ0p3ziJ1Hn75g')
					template_content = [
						{'content':nombre_concursante, 'name':'nombre_concursante'},
						{'content':cantidad_participantes, 'name':'cantidad_participantes'},
					]
					message = {
						'to':[
							{
								'email': email_concursante,
								'name': nombre_concursante,
								'type': 'to'
							}
						],
						'merge_language':'handlebars',
						'from_email':'andres@cpsingenieria.co',
						'merge_vars':[
							{
								'rcpt':email_concursante,
								'vars':[
									{'content':nombre_concursante, 'name':'nombre_concursante'},
									{'content':cantidad_participantes, 'name':'cantidad_participantes'},
								]
							}
						]
					}
					result = mandrill_client.messages.send_template(template_name='Test_cb_participantes', 
						template_content=template_content, message=message, async=False)
				except mandrill.Error, e:
					print 'A mandrill error occurred: %s - %s' % (e.__class__, e)

			return render(request, 'ruperton/terminos_aceptados.html')
		else:
			return render(request, 'ruperton/terminos_aceptados.html')
	else:
		return render(request, 'ruperton/terminos_vencidos.html')