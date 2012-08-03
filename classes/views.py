from classes.models import Classes

from django.shortcuts import render_to_response

def index(request):
	classes_list = Classes.objects.all()
	return render_to_response("classes.html", {"classes" : classes_list})
