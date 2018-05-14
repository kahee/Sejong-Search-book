from .base import *
import_secrets()

DEBUG = True
ALLOWED_HOSTS = [
    '.zoejoy.kr',
    '.elasticbeanstalk.com',
    '127.0.0.1',
    'localhost',
    '110.76.143.234',
    '110.76.143.235',
    '110.76.143.236',
    '172.31.27.153',
]
WSGI_APPLICATION = 'config.wsgi.production.application'
INSTALLED_APPS += [
    'django_extensions',
    'storages',
]

# Media(user-uploaded file)을 위한 스토리지
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFilesStorage'
# # Static files(collectstatic) 을 위한 스토리지
STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'
