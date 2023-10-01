from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home")

def carreras(request):
    return HttpResponse("Carreras")

def docentes(request):
    return HttpResponse("Docentes")
