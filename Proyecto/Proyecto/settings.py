import os
from pathlib import Path
from django.urls import reverse_lazy


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d-sxsbci0zd_ee76ito+#6x7pinv!8a-7^zoqy85bh6$c(h3-n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.usuario',
    'apps.mascota',
    'apps.adopcion',

]

THIRD_PARTY_APPS = [
    'rest_framework',
    'axes',
    'user_visit',
    'import_export',
    'simple_history',
    'captcha',
]


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'axes.middleware.AxesMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'user_visit.middleware.UserVisitMiddleware',
    
]

ROOT_URLCONF = 'Proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Proyecto.wsgi.application'




# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prueba2',#os.environ.get('DB_NAME'),#
        'USER': 'postgres',#os.environ.get('DB_USER'),#
        'PASSWORD': 'marcos2001',#os.environ.get('DB_PASSWORD'),#
        'HOST': 'localhost',#os.environ.get('DB_HOST'),
        'PORT': '5432',
    }
}

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'apps.usuario.views.MyBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        "OPTIONS":{'min_length':12},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

    {
        'NAME': 'Proyecto.customPassword.NumberValidator', 
        },
    {
        'NAME': 'Proyecto.customPassword.UppercaseValidator', 
        },
    {
        'NAME': 'Proyecto.customPassword.LowercaseValidator', 
        },
    {
        'NAME': 'Proyecto.customPassword.SymbolValidator', 
        },
]


AXES_FAILURE_LIMIT = 6
AXES_LOCK_OUT_AT_FAILURE = True
AXES_ONLY_USER_FAILURES = True
AXES_LOCKOUT_TEMPLATE = 'bloqueo.html'
AXES_RESET_ON_SUCCESS = True

# Internationalization
LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Guatemala'

USE_I18N = True

USE_L10N = True

USE_TZ = True


AUTH_USER_MODEL = 'usuario.User'


STATIC_URL = 'static/'
#STATIC_ROOT = '/code/static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('login')

APPEND_SLASH = False


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'refugiomascotasp@gmail.com'
EMAIL_HOST_PASSWORD = 'refugio980mascotas'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


#Captcha
RECAPTCHA_PUBLIC_KEY = '6LcGwYcfAAAAAL5RKPupSbbTxCJC2-ERwpeMtkG7'
RECAPTCHA_PRIVATE_KEY = '6LcGwYcfAAAAABSvVSPLKA3BT06SZEGDFFr_FU5x'
NOCAPTCHA= True