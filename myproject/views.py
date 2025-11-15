from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {}
    return render(request, template_name='home.html', context=context)

def about(request):
    context = {}
    return render(request, template_name='about.html', context=context)

def contact(request):
    context = {}
    return render(request, template_name='contact.html', context=context)

def hello(request):
    return HttpResponse("Hello from Django 5.2.7!")
