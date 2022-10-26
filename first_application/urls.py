#from django.conf.urls import url
from django.urls import path
from first_application import views

app_name = "first_application"

urlpatterns = [

    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
]
