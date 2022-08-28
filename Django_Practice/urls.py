
from django.contrib import admin
from django.urls import path
from first_application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('', views.index, name='index'),
]
