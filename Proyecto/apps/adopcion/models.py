from django.db import models
from simple_history.models import HistoricalRecords



from django.db import models


# Create your models here.


class Adoption(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    user = models.CharField('Usuario', max_length=150)
    firstName = models.CharField('Nombre', max_length=150)
    lastName = models.CharField('Apellido', max_length=150)
    email = models.EmailField('Email', max_length=150)
    
    phone = models.IntegerField('Número de Telefono')
    age = models.IntegerField('Edad')
    addreses = models.CharField('Dirección', max_length=150)
    Pet = models.OneToOneField("mascota.Pets", verbose_name='Mascota' ,blank=False, null=False, on_delete=models.CASCADE)
    reason = models.CharField('Motivo para adoptar', max_length=150)
    otherPets = models.IntegerField('Otras Mascotas',blank=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.user



class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=8)
    email = models.EmailField()
    domicilio = models.TextField()
    history = HistoricalRecords()

    
class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True,on_delete=models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()
    history = HistoricalRecords()
    