from django.urls import path
from portfolio.views import index, projects, about_me

urlpatterns = [
    path('', index, name='index'),
    path('projects/', projects, name='projects'),
    path('about_me/', about_me, name='about_me')
]
