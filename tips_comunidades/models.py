from django.db import models

# Create your models here.

class Tip_Comunidad(models.Model):
	tip = models.CharField(max_length=100)

	def __unicode__(self):
		return self.tip
