from django.urls import path
from . import views

urlpatterns = [
    path('foro/', views.foro_list, name='foro_list'),
    path('noticias/', views.noticia_list, name='noticia_list'),
]