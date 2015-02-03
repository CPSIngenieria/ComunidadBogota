from django.db.models.signals import post_save
from django.dispatch import receiver
from ruperton.models import Concursante

# @receiver(post_save, sender=Concursante, dispatch_uid="identificador_unico", weak=False)
def envio_correo_terminos(sender, **kwargs):
	import ipdb; ipdb.set_trace()
	print("Request finished!")

post_save.connect(envio_correo_terminos, sender=Concursante, dispatch_uid="identificador_unico", weak=False)
