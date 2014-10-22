from django.db import models

# Create your models here.

class Ruperto(models.Model):
	nombre = models.CharField(max_length=255)
	archivo_imagen = models.ImageField( upload_to = 'imagenes_rupertos')
	activo = models.BooleanField(default=False)

	def vista_ruperto_admin(self):
		return """
		<img src='%s' width='200' />
		""" % self.archivo_imagen.url

	vista_ruperto_admin.allow_tags = True

	def __unicode__(self):
		return self.nombre