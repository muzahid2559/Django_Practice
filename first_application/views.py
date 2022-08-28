from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>I am From First Application</h1>')

def contact(request):
    return HttpResponse('<h1>This is Contact Page</h1>')

def about(request):
    return HttpResponse('<h1>This is About Page</h1>')
