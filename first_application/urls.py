#from django.conf.urls import url
from django.urls import path
from first_application import views



app_name = "first_application"

urlpatterns = [
    # path('', views.index_test, name='index_test'), # function base url
    path('', views.IndexView.as_view(), name='IndexView'), # class base url
]
