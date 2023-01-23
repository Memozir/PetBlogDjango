import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ['www.potomverny.ru', 'potomverny.ru', '45.141.76.16']

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

SCRIPTS_DIR = os.path.join(STATIC_ROOT, 'scripts')
STATICFILES_DIRS = [SCRIPTS_DIR]

DB_NAME = os.getenv('NAME')
DB_USER = os.getenv('USER')
DB_PASS = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('HOST')

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': DB_NAME, #os.environ.get('NAME'),  #os.getenv('NAME'),
         'USER': DB_USER,  #os.getenv('USER'),
         'PASSWORD': DB_PASS,  #os.getenv('DB_PASSWORD'), #'esmiralda_>
         'HOST': DB_HOST,  #os.getenv('HOST'),
         'PORT': '',
     }
}
