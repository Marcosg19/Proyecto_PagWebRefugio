from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm




from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages




from django.http import HttpResponse

from .models import Adoption

from .forms import adoptionForm




def adoptionRequest(request):
    submitted = False
    if request.method == "POST":
        form = adoptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('adoptionRequest?submitted=True')
    else:
        form = adoptionForm(initial={'user': request.user})
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'adoptionrequest.html', {'form':form, 'submitted':submitted})    

def viewAdoption(request):
    adoption_list = Adoption.objects.all()

    return render(request, 'viewAdoption.html', {'adoption_list':adoption_list})


def deleteAdoption(request, Adoption_id):
    adoption = Adoption.objects.get(pk=Adoption_id)
    adoption.delete()
    return redirect('/viewAdoption')

def updateAdoption(request, Adoption_id):
    adoption = Adoption.objects.get(pk=Adoption_id)
    form = adoptionForm(request.POST or None, instance=adoption)
    if form.is_valid():
        form.save()
        messages.success(request, "Información actualizada")
        return redirect('/viewAdoption')
    
    return render(request, 'updateAdoption.html', {'adoption':adoption, 'form':form})












def index_adopcion(request):
	return HttpResponse("soy la pagina principal de la app adopcion")


class SolicitudList(ListView):
	model = Solicitud
	template_name = 'adopcion/solicitud_list.html'


class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopcion:solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))



class SolicitudUpdate(UpdateView):
	model = Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('adopcion:solicitud_listar')


	def get_context_data(self, **kwargs):
	    context = super(SolicitudUpdate, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    solicitud = self.model.objects.get(id=pk)
	    persona = self.second_model.objects.get(id=solicitud.persona_id)
	    if 'form' not in context:
	    	context['form'] = self.form_class()
	    if 'form2' not in context:
	    	context['form2'] = self.second_form_class(instance=persona)
	    context['id'] = pk
	    return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_solicitud = kwargs['pk']
		solicitud = self.model.objects.get(id=id_solicitud)
		persona = self.second_model.objects.get(id=solicitud.persona_id)
		form = self.form_class(request.POST, instance=solicitud)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


class SolicitudDelete(DeleteView):
	model = Solicitud
	template_name = 'adopcion/solicitud_delete.html'
	success_url = reverse_lazy('adopcion:solicitud_listar')

'''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Apps.adopcion.models import Persona, Solicitud
from Apps.adopcion.forms import PersonaForm, SolicitudForm
# Create your views here.

def index_adopcion(request):
    return HttpResponse("Esta es la pagina principal de la app adopcion")

class SolicitudList(ListView):
    model = Solicitud
    template_name='adopcion/solicitudList.html'

class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitudForm.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('solicitud_listar')

	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(UpdateView):
	model = Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitudForm.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('solicitud_listar')

	def get_context_data(self, **kwargs):
	    context = super(SolicitudUpdate, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    solicitud = self.model.objects.get(id=pk)
	    persona = self.second_model.objects.get(id=solicitud.persona_id)
	    if 'form' not in context:
	    	context['form'] = self.form_class()
	    if 'form2' not in context:
	    	context['form2'] = self.second_form_class(instance=persona)
	    context['id'] = pk
	    return 	

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_solicitud = kwargs['pk']
		solicitud = self.model.objects.get(id=id_solicitud)
		persona = self.second_model.objects.get(id=solicitud.persona_id)
		form = self.form_class(request.POST, instance=solicitud)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


class SolicitudDelete(DeleteView):
	model = Solicitud
	template_name = 'adopcion/solicitudDelete.html'
	success_url = reverse_lazy('solicitud_listar')
'''