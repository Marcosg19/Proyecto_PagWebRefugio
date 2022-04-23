from django import forms
from apps.adopcion.models import Persona, Solicitud



from django import forms
from .models import Adoption
from django.forms import ModelForm



class adoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = ('user','firstName','lastName','email','phone','age','addreses','Pet','reason','otherPets')
        
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'readonly ': ''}),
            'firstName': forms.TextInput(attrs={'class': 'form-control' }),
            'lastName': forms.TextInput(attrs={'class': 'form-control' }),
            'email': forms.EmailInput(attrs={'class': 'form-control' }),
            'phone': forms.NumberInput(attrs={'class': 'form-control' }),
            'age': forms.NumberInput(attrs={'class': 'form-control' }),
            'addreses': forms.TextInput(attrs={'class': 'form-control' }),
            'Pet': forms.Select(attrs={'class': 'form-control' }),
            'reason': forms.Textarea(attrs={'class': 'form-control','rows':'3' }),
            'otherPets': forms.Textarea(attrs={'class': 'form-control','rows':'3' }),

        }






class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos':'Apellidos',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio':'Domicilio',
        }
        widgets = {
            
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.Textarea(attrs={'class':'form-control'}),
        }


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'numero_mascotas': 'Numero de mascotas',
            'razones':'Razones para adoptar',
        }
        widgets = {            
            'numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
            'razones':forms.Textarea(attrs={'class':'form-control'}),
        }