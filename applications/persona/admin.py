from django.contrib import admin

from .models import Empleado, Habilidades

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    # Se indican las columnas que deseo que se muestren en el Administrador
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )

    def full_name(self, obj):
        # Se puede agregar toda la operación para crear una nueva columna en el Administrador
        return obj.first_name + ' ' + obj.last_name
        
    # Para búsquedas en el Administrador
    search_fields = ('first_name','last_name',)
    # Filtros que se visualizan en el Administrador
    list_filter = ('job','habilidades',)
    # Agrega un Filtro a un campo que es Muchos a Muchos
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
    