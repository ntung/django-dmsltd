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


def services(request, slug=None):
    def all_services():
        _list = {
            '/services/web-development': 'Web Development',
            '/services/mobile-app-development': 'Mobile App Development',
            '/services/data-analysis': 'Data Analysis',
            '/services/cloud-solutions': 'Cloud Solutions'
        }
    
        # content += "<p>Contact us for more information about our services.</p>"
        # content += "<p><a href='/httpobjects'>Creating Requests and Responses</a></p>"
        return _list

    services_info = {
        'web-development': 'We offer cutting-edge web development services using the latest technologies.',
        'mobile-app-development': 'Our mobile app development team creates user-friendly and high-performance apps.',
        'data-analysis': 'We provide comprehensive data analysis services to help you make informed decisions.',
        'cloud-solutions': 'Our cloud solutions ensure scalability, security, and efficiency for your business.'
    }
    selected_service = None
    content = None

    if slug is None:
        content = all_services()
    elif slug in services_info:
        selected_service = {
            'slug': slug,
            'title': slug.replace('-', ' ').title(),
            'description': services_info[slug]
        }
    else:
        pass  # Could handle unknown service slug here

    # return HttpResponse(content)
    context = {
        'services': services_info, 'content': content, 
        'selected_slug': slug, 'selected_service': selected_service, 
        'services_list': all_services()
    }
    return render(request, template_name='services.html', context=context)