from django.test import TestCase
from comunidades.models import Comunidad
# Create your tests here.

class TestComunidad(TestCase):

	def setUp(self):
		self.comunidad = Comunidad.objects.create(nombre='TestAutomatico')

	def test_existe_vista_admin(self):
		res = self.client.get('/admin/comunidades/comunidad/%d/' % self.comunidad.id)
		self.assertEqual(res.status_code, 302)