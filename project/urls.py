
from django.contrib import admin
from django.urls import path
from  app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_tareas/', views.lista_tareas, name='lista_tareas'),
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),

]
