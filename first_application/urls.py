#from django.conf.urls import url
from django.urls import path
from first_application import views



app_name = "first_application"

urlpatterns = [
    # path('', views.index_test, name='index_test'), # function base url
    path('', views.IndexView.as_view(), name='IndexView'), # class base url
    path('musician_details/<pk>/', views.MusicianDetail.as_view(), name='musician_details'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
    path('musician_update/<pk>/', views.UpdateMusician.as_view(), name='musician_update'),
    path('musician_delete/<pk>/', views.DeletMusician.as_view(), name='musician_delete'),
]
