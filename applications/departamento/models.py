from tabnanny import verbose
from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name= 'Departamento'
        verbose_name_plural= 'Departamentos'
        # Indica el orden en que quiero que se visualicen los datos
        ordering=['-name']
        # Indica los campos que se validen para que sean unicos
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name

