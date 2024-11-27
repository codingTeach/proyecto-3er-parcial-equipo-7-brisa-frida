from django.shortcuts import render
from django.http import JsonResponse
from .models import obtener_departamentos

urlpatterns = [
    path('api/departamentos/', views.obtener_departamentos_view),
]

# Create your views here.

def obtener_departamentos_view(request):
    departamentos = obtener_departamentos()
    return JsonResponse({'departamentos': departamentos})