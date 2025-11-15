from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def menu(request):
    content = "<h1 style='color: green'>My Menu</h1>"
    return HttpResponse(content)