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


def services(request):
    content = "<h1 style='color: green'>Our Services</h1>"
    content += "<ul>"
    content += "<li><a href='/service/web-development'>Web Development</a></li>"
    content += "<li><a href='/service/mobile-app-development'>Mobile App Development</a></li>"
    content += "<li><a href='/service/data-analysis'>Data Analysis</a></li>"
    content += "<li><a href='/service/cloud-solutions'>Cloud Solutions</a></li>"
    content += "</ul>"
    content += "<p>Contact us for more information about our services.</p>" 
    content += "<p><a href='/httpobjects'>Creating Requests and Responses</a></p>"
    return HttpResponse(content)

def servicedetails(request, service_slug=None):
    services_info = {
        'web-development': 'We offer cutting-edge web development services using the latest technologies.',
        'mobile-app-development': 'Our mobile app development team creates user-friendly and high-performance apps.',
        'data-analysis': 'We provide comprehensive data analysis services to help you make informed decisions.',
        'cloud-solutions': 'Our cloud solutions ensure scalability, security, and efficiency for your business.'
    }
    if service_slug in services_info:
        content = "<h1>Service Details</h1>"
        content += f"<h2>{service_slug.replace('-', ' ').title()}</h2>"
        content += f"<p>{services_info[service_slug]}</p>"
    else:
        content = "<h1>Service Not Found</h1>"
        content += "<p>The requested service does not exist. Please check the URL and try again.</p>"

    return HttpResponse(content)