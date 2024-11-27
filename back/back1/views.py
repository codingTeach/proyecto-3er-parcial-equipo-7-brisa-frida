from django.shortcuts import render
from django.http import JsonResponse
from .models import obtener_departamentos
from back.back1.models import MiModelo  
urlpatterns = [
    path('api/departamentos/', views.obtener_departamentos_view),
]

# Create your views here.

def obtener_departamentos_view(request):
    departamentos = obtener_departamentos()
    return JsonResponse({'departamentos': departamentos})
def obtener_profesores(request):
    profesores = Profesor.objects.all().values('nombre', 'apellido')
    return JsonResponse(list(profesores), safe=False)
