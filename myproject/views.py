import django
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
    context = {
        'django_version':  django.get_version(),
    }
    return render(request, template_name='welcome.html', context=context)
