from django.http import HttpResponse # make functional html

from django.shortcuts import render

# Create your views here.

def home_view(*args, **kwargs):
	return HttpResponse("<h1>hello world</h1>")