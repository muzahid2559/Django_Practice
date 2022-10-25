#from django.conf.urls import url
from django.urls import path
from first_application import views

app_name = "first_app"

urlpatterns = [

    path('', views.index, name='home'),
    path('form/', views.form, name='form'),
]
