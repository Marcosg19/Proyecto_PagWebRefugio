from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

app_name = 'adopcion'

urlpatterns = [
    re_path(r'^index$', index_adopcion),
    re_path(r'^solicitud/listar$', login_required(SolicitudList.as_view()), name='solicitud_listar'),
    re_path(r'^solicitud/nueva$', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    re_path(r'^solicitud/editar/(?P<pk>\d+)$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    re_path(r'^solicitud/eliminar/(?P<pk>\d+)$', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
    #path('index/', login_required(index_adopcion)),
    #path('solicitud/listar', login_required(SolicitudList.as_view()), name='solicitud_listar'),
    #path('solicitud/nueva', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    #path('solicitud/editar/<pk>/', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    #path('solicitud/eliminar/<pk>/', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]