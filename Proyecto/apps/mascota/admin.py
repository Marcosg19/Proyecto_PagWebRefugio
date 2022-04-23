from django.contrib import admin

from apps.mascota.models import Vacuna



from .models import Pets

# Register your models here.
admin.site.register(Pets)




admin.site.register(Vacuna)
#admin.site.register(Mascota)