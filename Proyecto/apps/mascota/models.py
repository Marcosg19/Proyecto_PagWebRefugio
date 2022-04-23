from django.db import models

#from apps.adopcion.models import Persona


from apps.usuario.models import User



class Pets(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    species = models.CharField('Especie', max_length=50)
    name = models.CharField('Nombre', max_length=50)
    sex = models.CharField('Sexo', max_length=20, choices=(
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ))
    breed = models.CharField('Raza', max_length=50)
    age = models.IntegerField('Edad')

    vaccination = models.CharField('Vacunacion', max_length=50)

    illness = models.CharField('Enfermedades', max_length=150)
    feeding = models.CharField('Alimentacion', max_length=150)
    rescue_date = models.DateField('Fecha de Rescate')
    description = models.CharField('Descripcion', max_length=150)

    adopter = models.ForeignKey(User, verbose_name='Adoptante' ,blank=True, null=True, on_delete=models.SET_NULL)
    
    #adopter = models.OneToOneField('Adoptante' , max_length=50)
    image = models.ImageField(default='pet.jpg', upload_to='pet_pics' , verbose_name='Foto')


    def __str__(self):
        return self.name








class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

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