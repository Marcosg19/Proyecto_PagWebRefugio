from django.urls import path, re_path
from .views import ListMascotasPDF, VacunaCreate, VacunaList, VacunaDelete, vacuna_edit, ListVacunaPDF, Pets

#from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, listado



from django.urls import path
from . import views 
from django.contrib.auth import views as authViews




app_name = 'mascota'


urlpatterns = [



    path('updatePet/<pet_id>', views.updatePet, name='updatePet'),
    path('deletePet/<pet_id>', views.deletePet, name='deletePet'),
    path('addPet', views.addPet, name='addPet'),
    path('viewPet', views.viewPet, name='viewPet'),
    path('nuevo-vacuna/', VacunaCreate.as_view(), name = "vacuna_crear"),
    path('listarvacuna/', VacunaList.as_view(), name = "vacuna_listar"),
    re_path(r'^editar-vacuna/(?P<id_vacuna>\d+)/', vacuna_edit, name = "vacuna_editar"),
    re_path(r'^vacuna-eliminar/(?P<pk>\d+)$', VacunaDelete.as_view(), name='vacuna_eliminar'),
    path('listarvacuna-pdf/', ListVacunaPDF.as_view(), name = "vacuna_listar_pdf"),
    path('listarmascota-pdf/', ListMascotasPDF.as_view(), name = "mascota_listar_pdf"),


]

    #path('', login_required(index), name='index'),
    #path('nuevo/', login_required(mascota_view), name='mascota_crear'),
    #path('nuevo2/', login_required(MascotaCreate.as_view()), name='mascota_crear2'),
    #path('listar/', login_required(mascota_list), name='mascota_listar'),
    #path('listar2', login_required(MascotaList.as_view()), name='mascota_listar2'),
    #path('editar/<id_mascota>/', login_required(mascota_edit), name='mascota_editar'),
    #path('editar2/<pk>/', login_required(MascotaUpdate.as_view()), name='mascota_editar2'),
    #path('eliminar/<id_mascota>/', login_required(mascota_delete), name='mascota_eliminar'),
    #path('eliminar2/<pk>/', login_required(MascotaDelete.as_view()), name='mascota_eliminar2'),
    #path('listado/', login_required(listado), name='listado'),