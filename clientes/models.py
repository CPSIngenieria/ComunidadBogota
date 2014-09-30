from django.db import models
from palabras_clave.models import PalabraClave
from comunidades.models import Comunidad

# Create your models here.

class Cliente(models.Model):

	razon_social = models.CharField( max_length = 255 )
	telefono = models.CharField( max_length = 255, blank = True )
	celular = models.CharField( max_length = 255, blank = True )
	direccion = models.CharField( max_length = 255, blank = True )
	sitio_web = models.URLField( blank = True )
	correo_electronico = models.EmailField( max_length = 254, blank = True )
	enlace_facebook = models.URLField( blank = True )
	enlace_twitter = models.URLField( blank = True )
	enlace_youtube = models.URLField( blank = True )
	inicio_horario_atencion = models.TimeField( blank = True )
	fin_horario_atencion = models.TimeField( blank = True )
	descripcion = models.TextField( max_length = 255, blank = True )
	logo = models.ImageField( upload_to = 'logos_clientes' )
	palabras_clave_inscritas = models.ManyToManyField( PalabraClave, blank = True )
	comunidad = models.ForeignKey( Comunidad )
	fecha_creacion = models.DateField( auto_now_add = True )

	def vista_logo_admin(self):
		return """
		<img src='%s' width='100' height='100' />
		""" % self.logo.url

	vista_logo_admin.allow_tags = True

	def esta_abierto(self):
		return True

	esta_abierto.boolean = True

	def __unicode__(self):
		return self.razon_social