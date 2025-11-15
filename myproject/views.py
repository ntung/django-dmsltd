from django.http import HttpResponse


def home(request):
    content = "<h1>Wellcome to Data Management Studio Limited Company!</h1>"
    return HttpResponse(content)
