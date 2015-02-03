from django.shortcuts import render

def ruperton_home(request):
	return render(request, 'ruperton/ruperton_home.html')
