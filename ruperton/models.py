from django.db import models

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
	numero_ganador_1_fecha_1 = models.PositiveIntegerField()
	numero_ganador_2_fecha_1 = models.PositiveIntegerField()
	numero_ganador_3_fecha_1 = models.PositiveIntegerField()
	numero_ganador_1_fecha_2 = models.PositiveIntegerField()
	numero_ganador_2_fecha_2 = models.PositiveIntegerField()
	numero_ganador_3_fecha_2 = models.PositiveIntegerField()
	numero_ganador_1_fecha_3 = models.PositiveIntegerField()
	numero_ganador_2_fecha_3 = models.PositiveIntegerField()
	numero_ganador_3_fecha_3 = models.PositiveIntegerField()
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

