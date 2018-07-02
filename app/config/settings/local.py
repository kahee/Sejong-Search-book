from .base import *

import_secrets()

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.local.application'

INSTALLED_APPS += [
    'django_extensions',
]

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DJANGO_DB_NAME', 'djangosample'),
#         'USER': os.environ.get('DJANGO_DB_USERNAME', 'sampleuser'),
#         'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'samplesecret'),
#         'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
#     }
# }
