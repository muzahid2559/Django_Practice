from django.shortcuts import render
from django.http import HttpResponse
from first_application.models import Musician, Album
from first_application import forms



# Create your views here.

def home(request):
    diction = {'simple_text':'This is a Simple Text', 'simple_num':'10'}
    return render(request,'first_application/home.html',context=diction)



def form(request):
    new_form = forms.MusicianForm()

    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    diction = {'test_form': new_form, 'heading_1':'Add New Musician'}
    return render(request,'first_application/form.html',context=diction)
