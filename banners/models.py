from django.db import models
from clientes.models import Cliente

# Create your models here.

class Banner(models.Model):

	archivo_banner = models.ImageField( upload_to = 'banners_clientes' )
	cliente = models.ForeignKey( Cliente )
	activo = models.BooleanField( default = False )
	fecha_vencimiento = models.DateField( blank = True )

	def vista_banner_admin(self):
		return """
		<img src='%s' width='300' height='100' />
		""" % self.archivo_banner.url

	vista_banner_admin.allow_tags = True

	def __unicode__(self):
		return self.cliente.razon_social