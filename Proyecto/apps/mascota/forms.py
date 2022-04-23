from django import forms
#from apps.mascota.models import Mascota



from django import forms
from .models import Pets
from django.forms import ModelForm



class addPetForm(ModelForm):
    class Meta:
        model = Pets
        fields = ('species','name','sex','breed','age','vaccination','illness','feeding','rescue_date','adopter','image','description')
        
        widgets = {
            'species': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'vaccination': forms.Textarea(attrs={'class': 'form-control','rows':'3' }),
            'illness': forms.Textarea(attrs={'class': 'form-control','rows':'2' }),
            'feeding': forms.Textarea(attrs={'class': 'form-control','rows':'2' }),
            'rescue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'adopter': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','rows':'3', }),
        }








'''
class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'raza',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels = {
            'nombre': 'Nombre',
            'raza' : 'Raza',
            'sexo':'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Adoptante',
            'vacuna':'Vacunas',
        }
        widgets = {
            
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'raza':forms.TextInput(attrs={'class':'form-control'}), 
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate':forms.TextInput(attrs={'class':'form-control'}),
            'persona':forms.Select(attrs={'class':'form-control'}),
            'vacuna':forms.CheckboxSelectMultiple(),
        }
'''