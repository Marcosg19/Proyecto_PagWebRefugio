from django.contrib import admin

from apps.adopcion.models import Persona

from .models import Adoption

admin.site.register(Adoption)

# Register your models here.
admin.site.register(Persona)