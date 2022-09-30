import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-y!k#j!)^G&SRDGY#&i0=9ui43q-0eklbfad6dxnuyt@%72114wn+'#os.getenv('SECRET_KEY') # 'django-insecure-y!k#j!)^G&SRDGY#&i0=9ui43q-0eklbfad6dxnuyt@$exuxmy%72114wn+'

DEBUG = False

ALLOWED_HOSTS = ['www.potomverny.ru', 'potomverny.ru']

# STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATICFILES_DIRS = [STATIC_DIR]
