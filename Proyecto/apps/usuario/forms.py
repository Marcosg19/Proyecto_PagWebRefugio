from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django import forms




class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}

class RegistroRForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
			]
		labels = {
				'username': 'Nombre de usuario',

		}

class captchaform(forms.Form):
    captcha = CaptchaField()