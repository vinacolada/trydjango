from django.http import HttpResponse # make functional html

from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs): # when you print args and kwargs you see a request (WSGIRequest) being passed as argument
	print(args, kwargs)
	print(request.user)
	return HttpResponse("<h1>hello world</h1>")

def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>contacts page</h1>")

def about_view(request, *args, **kwargs):
	return HttpResponse("<h1>about page</h1>")

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>social page</h1>")