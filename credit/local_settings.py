import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-y!k#j!)^G&SRDGY#&i0=9ui43q-0eklbfad6dxnuyt@$exuxmy%72114wn+'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),#'esmiralda_822',
        'HOST': os.getenv('HOST'),
        'PORT': '5432',
    }
}


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
