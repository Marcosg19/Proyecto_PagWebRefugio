import json
from rest_framework.views import APIView

from django.core import serializers
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.views.generic import CreateView, View
from django.urls import reverse_lazy

from apps.usuario.forms import RegistroForm, RegistroRForm
from apps.usuario.serializers import UserSerializer


from django.shortcuts import render, redirect
from .forms import ContactForm, captchaform
from django.contrib import messages
from Proyecto.printreports import render_to_pdf

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout ,get_user_model
from django.contrib import messages

from django.http import JsonResponse
from django.shortcuts import render
import threading
import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from django.contrib.auth import get_user_model

from django.http import HttpResponse

from .models import User, FailedLogin

from .forms import RegisterUserForm, captchaform, verifyUser
from axes.backends import AxesBackend

from apps.DeteccionRostro.DeteccionRostro  import CAPTURANDO , ENTRENANDO,RECONOCIENDO

User = get_user_model()

class MyBackend(AxesBackend):
    def authenticate(self, request=None, *args, **kwargs):
        if request:
            return super().authenticate(request, *args, **kwargs)

def home(request):
    return render(request, 'index.html')

def loginUser( request):
    if request.method == "POST":
        username = request.POST['userTextbox']
        password = request.POST['passwordTextbox']
        user = authenticate(request, username=username, password=password)        
             
        try:
            exist = User.objects.get(username=username)
        except:
            messages.success(request, "Usuario inexistente")
        if user is not None:
            FailedLogin.objects.filter(user = exist).delete()
            request.session['pk'] = user.pk
            # Redirect to a success page.
            
            return redirect('/verify')

        else: 
            
            if User.objects.filter(username=username).exists():
                print(username)
                if User.objects.get(username=username).is_active == False:
                    messages.success(request, "usuario bloqueado")
                else:
                    
                    try:
                        failex =FailedLogin.objects.get(user=exist)
                        failex.times += 1
                        failex.save()
                        print(FailedLogin.objects.get(user=exist).times)
                        if FailedLogin.objects.get(user=exist).times >= 6:
                            # three tries or more, disactivate the user
                            exist.is_active = False
                            exist.save()
                        elif FailedLogin.objects.get(user=exist).times == 3:
                            return redirect('/captcha')
                    except:
                        FailedLogin.objects.create(user=exist, times = 1)
                        
                    messages.success(request, "Contraseña incorrecta")
    return render(request, 'login.html')
    

def verify(request):
    form = verifyUser(request.POST or None)
    pk = request.session.get('pk')
    print(pk)
    if pk:
        user = User.objects.get(pk= pk)
                
        if form.is_valid():
            ENTRENANDO(user.username)
            RECONOCIENDO()
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
            
    return render(request, 'verifyUser.html', {'form':form,})
    

def logoutUser(request):
    logout(request)
    messages.success(request, "Adios")
    return redirect('/')

def registerUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, "registrado")
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            username = request.user.username
            CAPTURANDO(username)
            return redirect('/')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form':form,})

def captcha(request):
    if request.method == "POST":
        form = captchaform(request.POST)
        if form.is_valid():
            messages.success(request, "Correcto")
            return redirect('/login')
        else:
            messages.success(request, "Incorrecto")
    form = captchaform()
    return render(request, 'captcha.html', {'form':form,})


def viewClient(request):
    user = request.user
    if user.is_authenticated and user.is_superuser :
        Client_list = User.objects.all()
    else :
        Client_list = User.objects.filter(is_staff=False, is_superuser=False)

    return render(request, 'viewClient.html', {'Client_list':Client_list})



def deleteClient(request, Client_id):
    Client = User.objects.get(pk=Client_id)
    Client.delete()
    return redirect('/viewClient')
    
def updateProfile(request, Profile_id):
    Profile = User.objects.get(pk=Profile_id)
    form = RegisterUserForm(request.POST or None, request.FILES or None, instance=Profile)
    if form.is_valid():
        user =form.save()
        login(request,user, backend='django.contrib.auth.backends.ModelBackend')
        username = request.user.username
        CAPTURANDO(username)
        messages.success(request, "Información actualizada")
        return redirect('/')
    
    return render(request, 'updateProfile.html', {'Profile':Profile, 'form':form})





class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('login')



class RegistroRostro(CreateView):
	model = User
	template_name = "usuario/registrar_rostro.html"
	form_class = RegistroRForm
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

class ListaClientesPDF(View):
    def get(self, request, *args, **kwargs):
        clientes = User.objects.all()
		
        data = {
                'clientes': clientes,
                'cantidad': clientes.count()

        }
        pdf = render_to_pdf('pdf_clientes.html',data)
        return HttpResponse(pdf,content_type="application/pdf")


def captcha(request):
    if request.method == "POST":
        form = captchaform(request.POST)
        if form.is_valid():
            messages.success(request, "Correcto")
            return redirect('/login')
        else:
            messages.success(request, "Incorrecto")
    form = captchaform()
    return render(request, 'captcha.html', {'form':form,})

def contact(request):
    form = ContactForm(request.POST, request.FILES)

    if request.method == "POST":
        if form.is_valid():
            # Get all url files
            files = request.FILES.getlist("files")
            files_paths = get_paths_to_files_stored_in_memory(files)
            # Send email in background
            threading_emails = threading.Thread(
                target=send_email,
                    subject="Nuevo aviso",
                    to=["jose.goncas10@gmail.com"],
                    template_html="contact_email.html",
                    data={
                        "nombre": form.cleaned_data.get("nombre"),
                        "email": form.cleaned_data.get("email"),
                        "numero": form.cleaned_data.get("numero"),
                        "mensaje": form.cleaned_data.get("mensaje"),
                    },
                    attachments=files_paths,
            )
            threading_emails.start()
            # Response
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "ko", "errors": form.errors})
    return render(request, "index.html", {"form": form})

def send_email(
    subject="Nuevo aviso",
    to=[],
    template_txt="",
    template_html="",
    data={},
    attachments=[],
):
    """Send email"""
    msg = EmailMultiAlternatives(
        subject,
        render_to_string(template_txt, data),
        settings.DEFAULT_FROM_EMAIL,
        to,
    )
    msg.attach_alternative(render_to_string(template_html, data), "text/html")
    for attachment in attachments:
        msg.attach_file(attachment)
    msg.send()


def get_paths_to_files_stored_in_memory(files):
    """Get paths to files stored in memory"""

    def get_url_from_memory_file(file):
        path = default_storage.save("tmp/" + str(file), ContentFile(file.read()))
        return os.path.join(settings.MEDIA_ROOT, path)

    return list(map(get_url_from_memory_file, files))