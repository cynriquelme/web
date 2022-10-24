from django.db import models

from ckeditor.fields import RichTextField

from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad= models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural= 'Empleados'
        ordering=['-first_name']

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name

