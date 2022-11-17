import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ['www.potomverny.ru', 'potomverny.ru', '45.141.76.16']

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
<<<<<<< HEAD
SCRIPTS_DIR = os.path.join(STATIC_DIR, 'scripts')
STATICFILES_DIRS = [SCRIPTS_DIR]

=======
SCRIPTS_DIR = os.path.join(STATIC_ROOT, 'scripts')
STATICFILES_DIRS = [SCRIPTS_DIR]
>>>>>>> refs/remotes/potomv/main

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'credit_db',  #os.getenv('NAME'),
         'USER': 'postgres',  #os.getenv('USER'),
         'PASSWORD': '188558787356_t',  #os.getenv('DB_PASSWORD'), #'esmiralda_822',
         'HOST': '127.0.0.1',  #os.getenv('HOST'),
         'PORT': '',
     }
}
