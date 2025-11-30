from django.urls import path

from . import views
urlpatterns = [
    path('httpobjects/', views.httpobjects, name='httpobjects'),
    path('menu/', views.menu, name='menu'),
]