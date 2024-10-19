from django.shortcuts import render
from .models import Foro, Noticia

def foro_list(request):
    foros = Foro.objects.all()
    return render(request, 'foro/foro_list.html', {'foros': foros})

def noticia_list(request):
    noticias = Noticia.objects.all()
    return render(request, 'foro/noticia_list.html', {'noticias': noticias})