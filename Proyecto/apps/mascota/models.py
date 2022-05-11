from django.db import models

#from apps.adopcion.models import Persona

from apps.usuario.models import User
from simple_history.models import HistoricalRecords

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)
    history = HistoricalRecords()

    def __str__(self):
        return '{}'.format(self.nombre)


class Pets(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    especie = models.CharField('Especie', max_length=50)
    nombre = models.CharField('Nombre', max_length=50)
    sexo = models.CharField('Sexo', max_length=20, choices=(
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ))
    raza = models.CharField('Raza', max_length=50)
    edad = models.IntegerField('Edad')

    vacuna = models.ManyToManyField(Vacuna)

    enfermedades = models.CharField('Enfermedades', max_length=150)
    alimentacion = models.CharField('Alimentacion', max_length=150)
    rescate = models.DateField('Fecha de Rescate')
    descripcion = models.CharField('Descripcion', max_length=150)

    adopter = models.ForeignKey(User, verbose_name='Adoptante' ,blank=True, null=True, on_delete=models.SET_NULL)
    
    #adopter = models.OneToOneField('Adoptante' , max_length=50)
    image = models.ImageField(default='pet.jpg', upload_to='pet_pics' , verbose_name='Foto')
    history = HistoricalRecords()


    def __str__(self):
        return self.nombre










'''
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona,null=True,blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna,blank=True)
'''