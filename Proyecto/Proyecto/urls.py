from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView, logout_then_login

from django.urls import reverse_lazy


from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include, re_path
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth import views as authViews




urlpatterns = [
    path('', include('apps.mascota.urls')),
    path('', include('apps.adopcion.urls')),
    path('', include('apps.usuario.urls')),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
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
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



'''
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('' , LoginView.as_view(template_name= 'home.html'),name= 'home'),
    path('home/', LoginView.as_view(template_name= 'home1.html'),name= 'home1'),
    path('captcha/', include('captcha.urls')),
    re_path(r'^mascota/', include('apps.mascota.urls', namespace='mascota')),
    re_path(r'^adopcion/', include('apps.adopcion.urls', namespace='adopcion')),
    re_path(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
    #re_path(r'^accounts/login/', login, {'template_name':'index.html'}, name='login'),
    re_path(r'^accounts/login/',LoginView.as_view(template_name='index.html'),name='login'),
    re_path(r'^logout/', logout_then_login, name='logout'),


]
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
