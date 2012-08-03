from django.http import HttpResponse
from django.template import Context, loader
from classes.models import Classes

def index(request):
	classes_list = Classes.objects.all()
	template = loader.get_template("classes.html")
	c = Context({"classes" : classes_list})
	return HttpResponse(template.render(c));
