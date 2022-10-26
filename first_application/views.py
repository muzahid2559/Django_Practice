from django.shortcuts import render
from django.http import HttpResponse
from first_application.models import Musician, Album
from first_application import forms



# Create your views here.

def index(request):
    diction = {'title':'Home Page'}
    return render(request,'first_application/index.html',context=diction)

def album_list(request):
    diction = {'title':'List og Albums'}
    return render(request,'first_application/album_list.html',context=diction)

def musician_form(request):
    diction = {'title':'Add New Musician'}
    return render(request,'first_application/musician_form.html',context=diction)

def album_form(request):
    diction = {'title':'Add New Album'}
    return render(request,'first_application/album_form.html',context=diction)
