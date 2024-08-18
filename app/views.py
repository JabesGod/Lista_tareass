from django.shortcuts import render, redirect, get_object_or_404
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

def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == "POST":
        nuevo_titulo = request.POST.get('titulo')
        if nuevo_titulo:
            tarea.titulo = nuevo_titulo
            tarea.save()
        return redirect('lista_tareas')

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == "POST":
        tarea.delete()
        return redirect('lista_tareas')
