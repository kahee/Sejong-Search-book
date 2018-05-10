from .base import *

import_secrets()

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.local.application'

INSTALLED_APPS += [
    'django_extensions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
