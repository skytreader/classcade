from django.shortcuts import render_to_response

def index(request):
	data = {}
	data["style_list"] = ["index.css"]
	return render_to_response("index.html", data)
