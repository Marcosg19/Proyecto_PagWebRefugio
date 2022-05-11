from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.mascota.models import Vacuna
from .models import Pets

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Pets

class PetAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display= ('nombre','id')


# Register your models here.
admin.site.register(Pets, PetAdmin)

admin.site.register(Vacuna)
#admin.site.register(Mascota)