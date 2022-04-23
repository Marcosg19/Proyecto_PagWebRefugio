from django.contrib import admin


from django.contrib import admin
from .models import User
from .models import FailedLogin

# Register your models here.


class displayFailedLogin(admin.ModelAdmin):
    list_display =('user','times')
    
class displayUser(admin.ModelAdmin):
    list_display =('username','is_active','is_staff','is_superuser')

# Register your models here.
admin.site.register(User, displayUser)
admin.site.register(FailedLogin,displayFailedLogin)