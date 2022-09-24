from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    diction = {'text_1':'I am text send from views.py'}
    return render(request,'first_application/index.html',context=diction)
