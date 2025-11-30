from django.urls import path

from . import views
urlpatterns = [
    path('httpobjects/', views.httpobjects, name='httpobjects'),
    path('services/', views.services, name='services'),
    path('service/<str:service_slug>', views.servicedetails, name='servicedetails'),
]