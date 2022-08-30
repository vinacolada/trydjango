from django.http import HttpResponse # make functional html

from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs): # when you print args and kwargs you see a request (WSGIRequest) being passed as argument
	print(args, kwargs)
	print(request.user)
	# return HttpResponse("<h1>hello world</h1>")
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>social page</h1>")