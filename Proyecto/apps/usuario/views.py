import json
from rest_framework.views import APIView

from django.core import serializers
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuario.forms import RegistroForm
from apps.usuario.serializers import UserSerializer


class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:mascota_listar')


class UserAPI(APIView):
	serializer = UserSerializer

	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')



def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')