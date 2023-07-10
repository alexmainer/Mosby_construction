from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def services(request):
    return render(request, 'services.html')


def services_details(request):
    return render(request, 'service-details.html')


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    return render(request, 'projects.html')


def project_details(request):
    return render(request, 'project-details.html')
