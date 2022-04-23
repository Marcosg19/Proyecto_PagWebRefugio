from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django import forms




from cv2 import CAP_PVAPI_DECIMATION_2OUTOF16, resize
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from .models import User
from captcha.fields import CaptchaField


User = get_user_model()

class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2', 'image')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),

        }

class captchaform(forms.Form):
    captcha = CaptchaField()

class verifyUser(forms.Form):
    pass






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