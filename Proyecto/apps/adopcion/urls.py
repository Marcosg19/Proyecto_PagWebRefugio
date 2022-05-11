from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete, ListSolicitudesPDF




from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views 
from django.contrib.auth import views as authViews




app_name = 'adopcion'

urlpatterns = [



    path('adoptionRequest', views.adoptionRequest, name='adoptionRequest'),
    path('viewAdoption', views.viewAdoption, name='viewAdoption'),
    path('deleteAdoption/<Adoption_id>', views.deleteAdoption, name='deleteAdoption'),
    path('updateAdoption/<Adoption_id>', views.updateAdoption, name='updateAdoption'),
    path('solicitud/listar-pdf/', ListSolicitudesPDF.as_view(), name = "solicitud_listar_pdf"),




    #path('index/', login_required(index_adopcion)),
    #path('solicitud/listar', login_required(SolicitudList.as_view()), name='solicitud_listar'),
    #path('solicitud/nueva', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    #path('solicitud/editar/<pk>/', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    #path('solicitud/eliminar/<pk>/', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]