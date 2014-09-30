from django.db import models

# Create your models here.

class Comunidad(models.Model):

	nombre = models.CharField(max_length=255)

	def cantidad_inscritos(self):
		return self.cliente_set.count()

	cantidad_inscritos.admin_order_field = 'id'

	def __unicode__(self):
		return self.nombre