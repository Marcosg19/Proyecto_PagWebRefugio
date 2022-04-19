from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=8)
    email = models.EmailField()
    domicilio = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return '{}'.format(self.nombre+" "+self.apellidos)
    
class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True,on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
    history = HistoricalRecords()
    