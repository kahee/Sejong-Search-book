from .base import *

import_secrets()

DEBUG = True
ALLOWED_HOSTS = [
    '.zoejoy.kr',
    '.elasticbeanstalk.com',
    '127.0.0.1',
    'localhost',
]
WSGI_APPLICATION = 'config.wsgi.dev.application'

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

INSTALLED_APPS += [
    'django_extensions',
    'storages',
]

# Media(user-uploaded file)을 위한 스토리지
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFilesStorage'
# # Static files(collectstatic) 을 위한 스토리지
STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'
