import mandrill
import mailchimp
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from ruperton.models import Concursante, Sorteo, Residente, Compra

def ruperton_home(request):		
	sorteos = Sorteo.objects.all().order_by('-fecha_inicio_registro_compras')
	context = {
		'sorteos':sorteos,
	}
	return render(request, 'ruperton/ruperton_home.html',context)

def ruperton_residente(request, correo_residente):
	residente = get_object_or_404(Residente, correo=correo_residente)
	concursantes = Concursante.objects.filter(residente=residente).select_related('sorteo').order_by('-sorteo_id')
	context = {
		'residente':residente,
		'concursantes':concursantes,
	}
	return render(request, 'ruperton/ruperton_residente.html', context)

def ruperton_terminos(request, correo_residente, id_concursante):
	residente = get_object_or_404(Residente, correo=correo_residente)
	concursante = Concursante.objects.filter(residente=residente).get(pk=id_concursante)
	id_sorteo = concursante.sorteo.id
	sorteo = get_object_or_404(Sorteo, pk=id_sorteo)

	if sorteo.estado_sorteo == 'Cerrado':
		return render(request, 'ruperton/terminos_vencidos.html')
	if concursante.acepto_terminos:
		return render(request, 'ruperton/terminos_aceptados.html')
	else:
		context = {
			'nombre_concursante':concursante.residente.nombre,
			'correo_residente':correo_residente,
			'id_concursante':id_concursante,
		}
		return render(request, 'ruperton/terminos.html', context)

def ruperton_acepta_terminos(request):

	correo_residente = request.POST['correo_residente']
	id_concursante = request.POST['id_concursante']
	residente = get_object_or_404(Residente, correo=correo_residente)
	concursante = Concursante.objects.filter(residente=residente).get(pk=id_concursante)

	try:
		API_KEY = '890930f982cdd4aade758422f04ccc11-us10'
		api_mailchimp = mailchimp.Mailchimp(API_KEY)
		LIST_ID = concursante.sorteo.id_lista_correo
		api_mailchimp.lists.subscribe(LIST_ID,{'email':correo_residente})
	except mailchimp.ListAlreadySubscribedError:
		print("Este correo ya existe en la lista de mailchimp")
	except mailchimp.Error, e:
		print('Ocurrio un error en mailchimp: %s - %s' % (e.__class__, e))
	print("Se agrego el email satisfactoriamente")

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
			nombre_concursante = concursante_repetido.residente.nombre
			email_concursante = concursante_repetido.residente.correo

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

def ruperton_compras(request, correo_residente):
	residente = get_object_or_404(Residente, correo=correo_residente)
	compras = Compra.objects.filter(residente=residente)
	context = {
		'residente':residente,
		'compras':compras,
	}
	return render(request, 'ruperton/compras.html', context)

def ruperton_compras_registro(request):
	correo_residente = request.POST['correo_residente']
	establecimiento = request.POST['establecimiento']
	monto = request.POST['monto']

	residente = get_object_or_404(Residente, correo=correo_residente)
	nueva_compra = Compra(establecimiento=establecimiento, monto=monto, residente=residente)
	nueva_compra.save()
	compras = Compra.objects.filter(residente=residente)
	context = {
		'residente':residente,
		'compras':compras,
	}
	return render(request, 'ruperton/compras.html', context)

def user_login(request):

	username = request.POST['correo']
	password = request.POST['correo']

	user = authenticate(username=username, password=password)

	if user is not None:
		# Se verifico el password para el usuario especificado.
		if user.is_active:
			# El usuario esta activo:
			login(request, user)
			return HttpResponseRedirect(reverse('ruperton_home'))
		else: 
			# El usuario no esta activo
			context = {
				'login_error_message':"Lo sentimos, su cuenta no esta activa.",
			}
			return render(request, 'ruperton/login_form.html', context)
	else:
		# EL sistema de autenticacion no fue capaz de autenticar al usuario:
		context = {
				'login_error_message':"Usuario o contrasena incorrectas",
			}
		return render(request, 'ruperton/login_form.html', context)

def user_logout(request):

	logout(request)
	return HttpResponseRedirect(reverse('ComunidadBogotaView'))