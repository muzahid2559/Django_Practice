from django.shortcuts import render
from django.http import HttpResponse
from first_application.models import Musician, Album
from first_application import forms



# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':'This is a list of Musician', 'musician': musician_list}
    return render(request,'first_application/index.html',context=diction)



def form(request):
    new_form = forms.user_form()
    diction = {'test_form':new_form, 'heading_1':'This form is created using django library'}

    if request.method == 'POST':
        new_form = forms.user_form(request.POST)
        diction.update({'test_form':new_form})

        if new_form.is_valid():

            diction.update({'field':"Match!!"})
            diction.update({'form_submited' : 'Yes'})

    return render(request,'first_application/form.html',context=diction)
