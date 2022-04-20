from django.urls import path, re_path
#from django.contrib.auth.decorators import login_required

from apps.usuario.views import RegistroUsuario, UserAPI, RegistroRostro
from . import views

app_name = 'usuario'

urlpatterns = [
    re_path(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
    re_path(r'^registrar/rostro', RegistroRostro.as_view(), name="registrar_rostro"),
	re_path(r'^api', UserAPI.as_view(), name="api"),
    re_path(r'^captcha/', views.captcha,name='captcha'),
]

    #path('registrar/', RegistroUsuario.as_view(), name='usuario_registrar'),
    #path('listado/', login_required(listadousuarios), name='usuario_listado'),
    #path('api/', login_required(UserAPI.as_view()), name='api'),