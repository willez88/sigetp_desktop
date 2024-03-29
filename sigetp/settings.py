"""
Django settings for sigetp project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#a#q#x4m^zb0j*-j1s(%%#=y)&1cb@n0z=*%kbnvaq!i(v5nvv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

## Identifica a los administradores del sistema
ADMINS = [
    ('William Páez', 'wpaez@cenditel.gob.ve'),
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'base',
    'usuario',
    'vivienda',
    'vivienda.grupo_familiar',
    'vivienda.grupo_familiar.persona',
    'reporte',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sigetp.urls'

## Directorio en donde se encuentran las plantillas en el root de la aplicación
ROOT_TEMPLATES = os.path.join(BASE_DIR, "templates")

## Directorio en donde se encuentran las plantillas del módulo base
BASE_TEMPLATES = os.path.join(BASE_DIR, "base/templates")
USUARIO_TEMPLATES = os.path.join(BASE_DIR, "usuario/templates")
VIVIENDA_TEMPLATES = os.path.join(BASE_DIR, "vivienda/templates")
GRUPO_FAMILIAR_TEMPLATES = os.path.join(BASE_DIR, "vivienda/grupo_familiar/templates")
PERSONA_TEMPLATES = os.path.join(BASE_DIR, "vivienda/grupo_familiar/persona/templates")
REPORTE_TEMPLATES = os.path.join(BASE_DIR, "reporte/templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ROOT_TEMPLATES, BASE_TEMPLATES, USUARIO_TEMPLATES, GRUPO_FAMILIAR_TEMPLATES, PERSONA_TEMPLATES, REPORTE_TEMPLATES],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            #para usarlo con pyinstaller
            'libraries': {
                'i18n' : 'django.templatetags.i18n',
                'base_filters' : 'base.templatetags.base_filters',
            },
        },
    },
]

WSGI_APPLICATION = 'sigetp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'sigetp',
    #    'USER': 'admin',
    #    'PASSWORD': '123',
    #    'HOST': 'localhost',
    #    'PORT': '5432',
    #}
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

## Configuración del código del lenguaje a utilizar por defecto
LANGUAGE_CODE = 'es-ve'

## Configuración para el nombre de localización por defecto
LOCALE_NAME = 'es'

## Configuración para la zona horaria por defecto
TIME_ZONE = 'America/Caracas'

## Determina si se emplea la internacionalización I18N
USE_I18N = True

## Determina si se emplea la internacionalización L10N
USE_L10N = True

## Determina si se emplea la zona horaria
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

## Configuración de la raíz donde se encuentran los archivos estaticos del sistema (para entornos en producción)
STATIC_ROOT = ''

## Configuración de la url que atenderá las peticiones de los archivos estáticos del sistema
STATIC_URL = '/static/'

#MEDIA_URL = 'media/'
#MEDIA_ROOT = ''
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

## Configuración de los directorios en donde se encuentran los archivos estáticos
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    #os.path.join(BASE_DIR, 'media/'),
)

## URL de acceso al sistema
LOGIN_URL = "login"

LOGIN_REDIRECT_URL = 'inicio'

LOGOUT_REDIRECT_URL = 'login'

## URL de salida del sistema
#LOGOUT_URL = "/logout"

## configuración que permite obtener la ruta en donde se encuentran las traducciones de la aplicación a otros lenguajes
LOCALE_PATHS = [
    #os.path.join(BASE_DIR, 'locale'),
]

## Registro de mensajes al usuario
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'correo@gmail.com'
#EMAIL_HOST_PASSWORD = 'clave'
#EMAIL_FROM = EMAIL_HOST_USER
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
