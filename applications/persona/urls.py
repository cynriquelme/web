from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-area/<name>', views.ListAllEmpleadosArea.as_view()),
    path('buscar-empleado', views.ListAllEmpleadosByKword.as_view()),
]