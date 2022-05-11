from django.contrib import admin


from django.contrib import admin
from .models import User
from .models import FailedLogin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin (ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name', 'email', 'username']
    resources_class = CategoriaResource

class displayFailedLogin(admin.ModelAdmin):
    list_display =('user','times')
    
class displayUser(admin.ModelAdmin):
    list_display =('username','is_active','is_staff','is_superuser')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(FailedLogin,displayFailedLogin)