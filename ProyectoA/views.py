from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.template import Context, Template

def inicio(request):
    return HttpResponse("holitos :3")

def home(request):
    plantillaExterna = open("C:\MiProyecto\ProyectoA\ProyectoA\plantilla\index.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)