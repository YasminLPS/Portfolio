from django.urls import path
from portfolio.views import index, projetos

urlpatterns = [
    path('', index, name='index'),
    path('projetos/', projetos, name='projetos')
]
