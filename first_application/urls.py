#from django.conf.urls import url
from django.urls import path
from first_application import views

urlpatterns = [

    path('', views.index, name='home'),
    path('form/', views.form, name='form'),
]
