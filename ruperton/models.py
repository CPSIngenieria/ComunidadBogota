import mandrill
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Sorteo(models.Model):
	
	JUEGO='JU'
	ENTREGADO='EN'
	ACUMULADO='AC'
	ESTADOS_FECHAS = (
		(JUEGO, 'En juego'),
		(ENTREGADO, 'Entregado'),
		(ACUMULADO, 'Acumulado'),
	)

	JUGANDO='JU'
	INSCRIPCIONES='IN'
	CERRADO='CE'
	ESTADOS_SORTEOS = (
		(JUGANDO, 'En juego'),
		(INSCRIPCIONES, 'En inscripciones'),
		(CERRADO, 'Cerrado'),
	)

	fecha_creacion = models.DateField( auto_now_add = True )
	fecha_sorteo_1 = models.DateField( blank = True )
	fecha_sorteo_2 = models.DateField( blank = True )
	fecha_sorteo_3 = models.DateField( blank = True )
	premio_fecha_1 = models.PositiveIntegerField()
	premio_fecha_2 = models.PositiveIntegerField()
	premio_fecha_3 = models.PositiveIntegerField()
	numero_ganador_1_fecha_1 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_2_fecha_1 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_3_fecha_1 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_1_fecha_2 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_2_fecha_2 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_3_fecha_2 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_1_fecha_3 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_2_fecha_3 = models.PositiveIntegerField(blank=True, null=True)
	numero_ganador_3_fecha_3 = models.PositiveIntegerField(blank=True, null=True)
	estado_fecha_1 = models.CharField(max_length=2, choices=ESTADOS_FECHAS, default=JUEGO)
	estado_fecha_2 = models.CharField(max_length=2, choices=ESTADOS_FECHAS, default=JUEGO)
	estado_fecha_3 = models.CharField(max_length=2, choices=ESTADOS_FECHAS, default=JUEGO)
	estado_sorteo = models.CharField(max_length=2, choices=ESTADOS_SORTEOS, default=INSCRIPCIONES)

	def __unicode__(self):
		return str(self.id) + " - " + self.estado_sorteo
	def nombre_sorteo(self):
		return str(self.id) + " - " + self.estado_sorteo

class Concursante(models.Model):
	nombre = models.CharField(max_length=100)
	correo = models.EmailField()
	direccion = models.CharField(max_length=255)
	telefono = models.CharField( max_length = 255 )
	establecimiento = models.CharField( max_length = 255, blank = True )
	numero_ganador_1 = models.PositiveIntegerField()
	numero_ganador_2 = models.PositiveIntegerField()
	numero_ganador_3 = models.PositiveIntegerField()
	acepto_terminos = models.BooleanField( default = False )
	sorteo = models.ForeignKey(Sorteo)

	def __unicode__(self):
		return self.nombre

# @receiver(post_save, sender=Concursante, dispatch_uid="identificador_unico", weak=False)
def envio_correo_terminos(sender, **kwargs):
	
	concursante = kwargs.get('instance')
	nombre_concursante = concursante.nombre
	email_concursante = concursante.correo	
	acepto_terminos = concursante.acepto_terminos
	link_terminos_concursante = "http://comunidadbogota.com/ruperton/terminos/%s/" % concursante.id

	# Enviamos un correo electronico con la informacion del concursante y el link de los terminos:
	if not acepto_terminos:
		try:
			mandrill_client = mandrill.Mandrill('_SoGpYeWNJ0p3ziJ1Hn75g')
			template_content = [
				{'content':nombre_concursante, 'name':'nombre_concursante'},
				{'content':link_terminos_concursante, 'name':'link_terminos'},
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
							{'content':link_terminos_concursante, 'name':'link_terminos'},
						]
					}
				]
			}
			result = mandrill_client.messages.send_template(template_name='Test_cb_terminos', 
				template_content=template_content, message=message, async=False)
		except mandrill.Error, e:
			print 'A mandrill error occurred: %s - %s' % (e.__class__, e)

post_save.connect(envio_correo_terminos, sender=Concursante, dispatch_uid="identificador_unico", weak=False)
