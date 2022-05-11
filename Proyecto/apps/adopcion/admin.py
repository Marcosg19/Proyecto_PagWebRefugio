from django.contrib import admin

from apps.adopcion.models import Persona

from .models import Adoption

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Persona

class PersonaAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display= ('nombre','apellidos','edad','telefono')

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Adoption

class AdoptionAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['user']
    list_display= ('firstName','addreses','email','Pet','reason')


admin.site.register(Adoption, AdoptionAdmin)
admin.site.register(Persona, PersonaAdmin)
