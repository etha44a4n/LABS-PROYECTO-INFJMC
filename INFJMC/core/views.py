from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    title = "Home"
    data = {
        'title': title
    }
    return render(request, 'core/home.html', data)

def carreras(request):
    title = "Carreras"
    data = {
        'title': title
    }
    return render(request, 'core/carreras.html', data)

def docentes(request):
    title = "Docentes"
    data = {
        'title': title
    }
    return render(request, 'core/docentes.html', data)
