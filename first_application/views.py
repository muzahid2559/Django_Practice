from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>This is Homepage</h1> <a href="contact/">Contact</a> <a href="about/">About</a>')

def contact(request):
    return HttpResponse('<h1>This is Contact Page</h1> <a href="/">Home</a> <a href="/about/">About</a>')

def about(request):
    return HttpResponse('<h1>This is About Page</h1> <a href="/">Home</a> <a href="/contact/">Contact</a>')
