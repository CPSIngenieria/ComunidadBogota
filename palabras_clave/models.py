from django.db import models

# Create your models here.

class PalabraClave(models.Model):

	descripcion = models.CharField( max_length = 100 )

	def cantidad_inscritos(self):
		return self.cliente_set.count()

	cantidad_inscritos.order_admin_field = 'id'

	def __unicode__(self):
		return self.descripcion