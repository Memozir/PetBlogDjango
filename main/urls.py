from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('service_find/', views.service_find, name='service_find')
]
