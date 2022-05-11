from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, request, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

#from apps.mascota.forms import MascotaForm
#from apps.mascota.models import Mascota

#from weasyprint import HTML
#from weasyprint.text.fonts import FontConfiguration
from Proyecto.printreports import render_to_pdf
from .forms import VacunaForm
from .models import Vacuna
from django.urls import reverse_lazy




from django.shortcuts import render, redirect

from django.contrib import messages


from django.http import HttpResponse

from .models import Pets

from .forms import addPetForm


# Views

class VacunaCreate(CreateView):
	model = Vacuna
	template_name = 'vacuna/vacuna_form.html'
	form_class = VacunaForm
	success_url = reverse_lazy('mascota:vacuna_listar')

    
	def get_context_data(self, **kwargs):
		context = super(VacunaCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			solicitud = form.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form)) 

class ListMascotasPDF(View):
    def get(self, request, *args, **kwargs):
        mascota = Pets.objects.all()
        data = {
                'Pets': mascota,
                'cantidad': mascota.count()
        }
        pdf = render_to_pdf('pdf_mascota.html',data)
        return HttpResponse(pdf,content_type="application/pdf")

class ListVacunaPDF(View):
    def get(self, request, *args, **kwargs):
        vacuna = Vacuna.objects.all()
        data = {
                'vacunas': vacuna,
                'cantidad': vacuna.count()
        }
        pdf = render_to_pdf('vacuna/pdf_vacuna.html',data)
        return HttpResponse(pdf,content_type="application/pdf")


class VacunaList(ListView):
	model = Vacuna
	template_name = 'vacuna/vacuna_list.html'
	paginate_by = 5

class VacunaDelete(DeleteView):
	model = Vacuna
	template_name = 'vacuna/vacuna_delete.html'
	success_url = reverse_lazy('mascota:vacuna_listar')

def vacuna_edit(request, id_vacuna):
    vacuna = Vacuna.objects.get(id = id_vacuna)
    if request.method == 'GET':
        form = VacunaForm(instance=vacuna)
    else:
        form = VacunaForm(request.POST, files=request.FILES,instance = vacuna)
        if form.is_valid():
            form.save()
        return redirect('vacuna_listar')
    return render(request, 'vacuna/vacuna_form.html',{'form':form})


def viewPet(request):
    pet_list = Pets.objects.all()
    return render(request, 'viewpet.html', {'pet_list':pet_list})


def addPet(request):    
    if request.method == "POST":
        form = addPetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mascota ingresada")
            return redirect('/addPet')
    else:
        form = addPetForm()
    return render(request, 'addpet.html', {'form':form})

def updatePet(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    form = addPetForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save()
        messages.success(request, "Información actualizada")
        return redirect('/viewPet')
    
    return render(request, 'updatepet.html', {'pet':pet, 'form':form})


def deletePet(request, pet_id):
    pet = Pets.objects.get(pk=pet_id)
    pet.delete()
    
    return redirect('/viewPet')
