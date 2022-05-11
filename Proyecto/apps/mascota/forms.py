from django import forms
#from apps.mascota.models import Mascota



from django import forms
from .models import Pets, Vacuna
from django.forms import ModelForm

class VacunaForm(forms.ModelForm):

	class Meta:
		model = Vacuna
		fields = [
			'nombre',			
		]
		labels = {
			'nombre': 'Nombre de la Vacuna',
					
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
		}


class addPetForm(ModelForm):
    class Meta:
        model = Pets
        fields = ('especie','nombre','sexo','raza','edad','vacuna','enfermedades','alimentacion','rescate','adopter','image','descripcion')
        
        widgets = {
            'especie': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
            'enfermedades': forms.Textarea(attrs={'class': 'form-control','rows':'2' }),
            'alimentacion': forms.Textarea(attrs={'class': 'form-control','rows':'2' }),
            'rescate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'adopter': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','rows':'3', }),
        }
