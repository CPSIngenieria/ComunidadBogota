import mandrill
import mailchimp
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.models import User

class Residente(models.Model):
	nombre = models.CharField( max_length=100)
	cedula = models.CharField( max_length=100)
	correo = models.EmailField(unique=True)
	direccion = models.CharField( max_length=100)
	telefono = models.CharField( max_length=100)

	def __unicode__(self):
		return self.nombre + " - " + self.correo

class Compra(models.Model):
	fecha_registro = models.DateTimeField(auto_now_add=True)
	establecimiento = models.CharField(max_length=255)
	monto = models.PositiveIntegerField()
	residente = models.ForeignKey(Residente)

	def __unicode__(self):
		return self.residente.nombre + ' - ' + '{:,}'.format(self.monto)

	def nombre_residente(self):
		return self.residente.nombre

class Ganador(models.Model):
	residente = models.ForeignKey(Residente)
	foto = models.ImageField(upload_to='fotos_ganadores')
	fecha = models.DateField(auto_now_add=True)
	establecimiento = models.CharField(max_length=100)

	def __unicode__(self):
		return self.residente.nombre + "-" + str(self.fecha)

	def foto_admin(self):
		return """
		<img src='%s' width='300' height='200' />
		""" % self.foto.url
	foto_admin.allow_tags = True

class Sorteo(models.Model):
	
	JUEGO='Jugando'
	ENTREGADO='Cerrado'
	ESTADOS_FECHAS = (
		(JUEGO, 'En juego'),
		(ENTREGADO, 'Cerrado'),
	)

	JUGANDO='Jugando'
	CERRADO='Cerrado'
	ESTADO_SORTEO = (
		(JUGANDO, 'En juego'),
		(CERRADO, 'Cerrado'),
	)

	estado_sorteo = models.CharField(max_length=50, choices=ESTADO_SORTEO, default=JUGANDO)
	nombre = models.CharField(max_length=100)
	id_lista_correo = models.CharField(max_length=100)
	fecha_inicio_registro_compras = models.DateField()
	fecha_cierre_registro_compras = models.DateField()
	
	fecha_sorteo_1 = models.DateField( blank = True )
	estado_sorteo_1 = models.CharField(max_length=50, choices=ESTADOS_FECHAS, default=JUEGO)
	premio_sorteo_1 = models.CharField(max_length=20)
	numero_ganador_1_sorteo_1 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_2_sorteo_1 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_3_sorteo_1 = models.PositiveIntegerField(blank=True, null=True)
	ganador_sorteo_1 = models.ManyToManyField(Ganador, related_name='ganador_sorteo_1', blank=True)
	
	fecha_sorteo_2 = models.DateField( blank = True )
	estado_sorteo_2 = models.CharField(max_length=50, choices=ESTADOS_FECHAS, default=JUEGO)
	premio_sorteo_2 = models.CharField(max_length=20)
	numero_ganador_1_sorteo_2 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_2_sorteo_2 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_3_sorteo_2 = models.PositiveIntegerField(blank=True, null=True)
	ganador_sorteo_2 = models.ManyToManyField(Ganador, related_name='ganador_sorteo_2', blank=True)
	
	premio_registro_compras = models.CharField(max_length=20)
	ganador_registro_compras = models.ManyToManyField(Ganador, related_name='ganador_sorteo_compras', blank=True)

	def __unicode__(self):
		return self.nombre + " - " + self.estado_sorteo

class Concursante(models.Model):
	establecimiento = models.CharField(max_length=255)
	numero_ganador_1 = models.PositiveIntegerField()
	numero_ganador_2 = models.PositiveIntegerField()
	numero_ganador_3 = models.PositiveIntegerField()
	acepto_terminos = models.BooleanField( default = False )
	sorteo = models.ForeignKey(Sorteo)
	residente = models.ForeignKey(Residente)

	def __unicode__(self):
		return self.residente.nombre + ' - ' + self.sorteo.nombre

	def nombre_concursante(self):
		return self.residente.nombre
	def correo_concursante(self):
		return self.residente.correo
	def numeros_seleccionados(self):
		return str(self.numero_ganador_1) + "," + str(self.numero_ganador_2) + "," + str(self.numero_ganador_3)

def agregar_a_lista_de_correo_total(sender, **kwargs):
	
	residente = kwargs.get('instance')
	correo_residente = residente.correo
	try:
		API_KEY = '1f86e78c19bf0dea21f39928412e0bb4-us10'
		api_mailchimp = mailchimp.Mailchimp(API_KEY)
		LIST_ID = '8ccd5f4ac6'
		api_mailchimp.lists.subscribe(LIST_ID,{'email':correo_residente})
	except mailchimp.ListAlreadySubscribedError:
		print("Este correo ya existe en la lista de mailchimp")
	except mailchimp.Error, e:
		print('Ocurrio un error en mailchimp: %s - %s' % (e.__class__, e))
	print("Se agrego el email satisfactoriamente")

post_save.connect(agregar_a_lista_de_correo_total, sender=Residente, dispatch_uid="identificador_unico", weak=False)


def envio_correo_terminos(sender, **kwargs):
	
	concursante = kwargs.get('instance')
	nombre_concursante = concursante.residente.nombre
	email_concursante = concursante.residente.correo
	numero_1 = concursante.numero_ganador_1	
	numero_2 = concursante.numero_ganador_2	
	numero_3 = concursante.numero_ganador_3	
	acepto_terminos = concursante.acepto_terminos
	link_terminos_concursante = "http://comunidadbogota.com/ruperton/terminos/%s/%s/" % (email_concursante, concursante.id)

	# Enviamos un correo electronico con la informacion del concursante y el link de los terminos:
	if not acepto_terminos:
		try:
			mandrill_client = mandrill.Mandrill('zR3BBjwQJM2qv8IiJe6Scg')
			template_content = [
				{'content':nombre_concursante, 'name':'nombre_concursante'},
				{'content':link_terminos_concursante, 'name':'link_terminos'},
				{'content':numero_1, 'name':'numero_1'},
				{'content':numero_2, 'name':'numero_2'},
				{'content':numero_3, 'name':'numero_3'},
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
				'from_email':'comunidadcedritos@hotmail.com',
				'merge_vars':[
					{
						'rcpt':email_concursante,
						'vars':[
							{'content':nombre_concursante, 'name':'nombre_concursante'},
							{'content':link_terminos_concursante, 'name':'link_terminos'},
							{'content':numero_1, 'name':'numero_1'},
							{'content':numero_2, 'name':'numero_2'},
							{'content':numero_3, 'name':'numero_3'},
						]
					}
				]
			}
			result = mandrill_client.messages.send_template(template_name='Terminos_ruperton', 
				template_content=template_content, message=message, async=True)
		except mandrill.Error, e:
			print 'A mandrill error occurred: %s - %s' % (e.__class__, e)

post_save.connect(envio_correo_terminos, sender=Concursante, dispatch_uid="identificador_unico_terminos", weak=False)

def crear_usuario(sender, **kwargs):
	
	residente = kwargs.get('instance')
	correo_residente = residente.correo
	User.objects.create_user(correo_residente,correo_residente,correo_residente)

post_save.connect(crear_usuario, sender=Residente, dispatch_uid="identificador_unico_crear", weak=False)