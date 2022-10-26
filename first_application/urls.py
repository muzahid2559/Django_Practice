#from django.conf.urls import url
from django.urls import path
from first_application import views

app_name = "first_application"

urlpatterns = [

    path('', views.index, name='index'),
    path('add_musician/', views.musician_form, name='musician_form'),
        path('add_album/', views.album_form, name='album_form'),
]
