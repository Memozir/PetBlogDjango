import os
from .settings import BASE_DIR


DEBUG = True

ALLOWED_HOSTS = []

# STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
SCRIPTS_DIR = os.path.join(STATIC_ROOT, 'scripts')
STATICFILES_DIRS = [SCRIPTS_DIR]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
