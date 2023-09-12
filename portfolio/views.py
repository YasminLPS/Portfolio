from django.shortcuts import render, redirect
from .models import ContactMe
from django.http import HttpResponse
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage

def sendmail_contact(data):
    message_body = get_template('send.html').render(data)
    email = EmailMessage('Formulario de Contato', message_body, settings.DEFAULT_FROM_EMAIL, to=['yasminportfolio@outlook.com'])
    email.content_subtype = "html"
    return email.send()

def index(request):
    if request.method == "POST":
        contact = ContactMe()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'subject': request.POST.get('subject') 
            
        }
        sendmail_contact(data)
        
        
        return redirect('index')
        
    return render(request, 'portfolio/index.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def about_me(request):
    return render(request, 'portfolio/about_me.html')

def contact(request):
     return render(request, 'portfolio/contact.html')
    