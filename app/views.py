from django.shortcuts import render, redirect
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})

def agregar_tarea(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        if titulo:
            Tarea.objects.create(titulo=titulo)
        return redirect('lista_tareas')
    return render(request, 'agregar_tarea.html')
