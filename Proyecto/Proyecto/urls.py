"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView, logout_then_login
from django.urls import include, path, re_path


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^mascota/', include('apps.mascota.urls', namespace='mascota')),
    re_path(r'^adopcion/', include('apps.adopcion.urls', namespace='adopcion')),
    re_path(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
    #re_path(r'^accounts/login/', login, {'template_name':'index.html'}, name='login'),
    re_path(r'^accounts/login/',LoginView.as_view(template_name='index.html'),name='login'),
    re_path(r'^logout/', logout_then_login, name='logout'),
    re_path(r'^reset/password_reset', PasswordResetView.as_view(), 
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'}, 
        name='password_reset'), 
    re_path(r'^password_reset_done', PasswordResetDoneView.as_view(), 
        {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    re_path(r'^reset/done', PasswordResetCompleteView.as_view(), {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),

]
