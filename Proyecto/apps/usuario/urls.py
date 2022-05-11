from django.urls import path, re_path
#from django.contrib.auth.decorators import login_required

#from apps.usuario.views import RegistroUsuario, UserAPI, RegistroRostro
from . import views

from .views import ListaClientesPDF
from django.urls import path
from . import views 
#from django.contrib.auth import views as authViews





app_name = 'usuario'

urlpatterns = [
    path('', views.home, name='Inicio'),
    path('login', views.loginUser, name='login'),
    path('verify', views.verify, name='verify'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),
    

    path('viewClient', views.viewClient, name='viewClient'),
    path('deleteClient/<Client_id>', views.deleteClient, name='deleteClient'),
    path('updateProfile/<Profile_id>', views.updateProfile, name='updateProfile'),
    path('listarclientes-pdf/', ListaClientesPDF.as_view(), name = "clientes_listar_pdf"),

       #? passsword reset email
    
        # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    
    
    path('captcha', views.captcha,name='captcha'),
    path('contacto', views.contact, name='contact')
]

    #path('registrar/', RegistroUsuario.as_view(), name='usuario_registrar'),
    #path('listado/', login_required(listadousuarios), name='usuario_listado'),
    #path('api/', login_required(UserAPI.as_view()), name='api'),

'''
    path('password_change/done/', authViews.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', authViews.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', authViews.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    
    
    path('password_reset/', authViews.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', authViews.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),
'''