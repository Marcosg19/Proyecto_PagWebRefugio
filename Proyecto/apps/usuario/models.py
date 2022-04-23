from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    CHOICES = (
        ('admin', 'Administrador'),
        ('colab', 'Colaborador'),
        ('client', 'Usuario'),
    )

    role = models.CharField(max_length=300, choices=CHOICES, default='client',)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Foto de perfil')


class FailedLogin(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, db_column='username')
    times = models.IntegerField('Times', default='0')
    timestamp = models.DateTimeField(auto_now_add=True)
