from django.shortcuts import render
from django.views.generic import (
    ListView
)

# models
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    context_object_name = 'lista'

class ListAllEmpleadosArea(ListView):
    # Listado de empleados de un área
    template_name = 'persona/list_all_area.html'

    def get_queryset(self):
        area = self.kwargs['name']
        lista = queryset = Empleado.objects.filter(
            departamento__name = area
        )
        return lista

class ListAllEmpleadosByKword(ListView):
    # Lista de empleados por palabra clave
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista