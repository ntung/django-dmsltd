from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def httpobjects(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.get_host() # Get user agent info: request.META['REMOTE_ADDR']]
    user_agent = request.META['HTTP_USER_AGENT'] 
    path_info = request.META['PATH_INFO'] # Additional path info: request.path_info

    response = HttpResponse(content_type='text/html; charset=utf-8', charset='utf-8')
    response.headers['Custom-Header'] = 'This is a custom header'
    response.headers['Age'] = 20

    content = "<h1>Creating Requests and Responses</h1>"
    content += f"<p>Path: {path}</p>"
    content += f"<p>Scheme: {scheme}</p>"
    content += f"<p>Method: {method}</p>"
    content += f"<p>Address: {address}</p>"
    content += f"<p>User Agent: {user_agent}</p>"
    content += f"<p>Path Info: {path_info}</p>"
    content += f"<p>Response Headers: {response.headers}</p>"
    response.content = content

    return response
    # return render(request, 'home.html', {'name': 'Rahul'})


def menu(request):
    content = "<h1 style='color: green'>My Menu</h1>"
    return HttpResponse(content)