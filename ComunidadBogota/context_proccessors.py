from random import choice

frases = ['Hola!', 'Soy Rupert', 'Busca una palabra clave']

def testCP(request):

	# return {'usuario':'andresito'}
	return {'usuario':choice(frases)}