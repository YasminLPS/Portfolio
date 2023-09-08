from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def about_me(request):
    return render(request, 'portfolio/about_me.html')