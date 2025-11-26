from django.shortcuts import render
from django.http import HttpResponse

# Ruta 1: Mensaje simple
def vista_pruebas(request):
    return HttpResponse("<h1>Bienvenido a Django desde unitecnar</h1>")

# Ruta 2: HTML completo
def vista_template(request):
    return render(request, 'index.html')
