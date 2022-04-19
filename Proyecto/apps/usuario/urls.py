from django.urls import path, re_path
#from django.contrib.auth.decorators import login_required

from apps.usuario.views import RegistroUsuario, UserAPI

app_name = 'usuario'

urlpatterns = [
    re_path(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
	re_path(r'^api', UserAPI.as_view(), name="api"),
]

    #path('registrar/', RegistroUsuario.as_view(), name='usuario_registrar'),
    #path('listado/', login_required(listadousuarios), name='usuario_listado'),
    #path('api/', login_required(UserAPI.as_view()), name='api'),