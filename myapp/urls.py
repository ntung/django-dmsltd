from django.urls import path

from . import views
urlpatterns = [
    path('httpobjects/', views.httpobjects, name='httpobjects'),
    path('services/', views.services, name='services'),
    path('services/<str:slug>', views.services, name='services'),
]