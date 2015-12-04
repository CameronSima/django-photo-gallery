"""
Django settings for pornsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from photologue import PHOTOLOGUE_APP_DIR

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TOP_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fyz1*u90honxt5ahy12l(jp2zz)9rmho4zfqs2wzcm)@qpdev)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.csrf',
    'django.core.context_processors.media',
)



TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)



TEMPLATE_DIRS = (
    PHOTOLOGUE_APP_DIR,
)

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    #South not needed for Django>1.7
    'sortedm2m',
    'photologue',
    'registration',
    'taggit',
    'paypal.standard.ipn',
    
)

LOCAL_APPS = (
    'pornsite',
    'galleries',
    'photologue_custom',

)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pornsite.urls'

WSGI_APPLICATION = 'pornsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'postgres',
        'PASSWORD': 'simc102011',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/




#MEDIA_ROOT = 'media/'

STATIC_ROOT = os.path.join(TOP_FOLDER, 'public', 'media/')
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(TOP_FOLDER, 'public', 'static')

MEDIA_URL = '/media/'

SITE_ID = 1

ACCOUNT_ACTIVATION_DAYS = '7'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PAYPAL_RECEIVER_EMAIL = 'cjsima-facilitator@gmail.com'

PAYPAL_ID = 'simaburgosphotography@gmail.com'

PHOTOLOGUE_GALLERY_SAMPLE_SIZE = 1