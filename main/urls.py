from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('service_find/', views.ServiceFindFormView.as_view(), name='service_find')
    # path('service_find/', views.service_find, name='service_find')
]
