from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def projetos(request):
    return render(request, 'portfolio/projetos.html')