from django.shortcuts import render
from django.http import HttpResponse
from first_application.models import Musician, Album
from first_application import forms



# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by("first_name") #Select Query Kaj Kore
    diction = {'title':'Home Page', 'musician_list':musician_list}
    return render(request,'first_application/index.html',context=diction)

def album_list(request):
    diction = {'title':'List of Albums'}
    return render(request,'first_application/album_list.html',context=diction)

def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title':'Add New Musician', 'musician_form':form}
    return render(request,'first_application/musician_form.html',context=diction)


def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title':'Add New Album', 'album_form':form}
    return render(request,'first_application/album_form.html',context=diction)
