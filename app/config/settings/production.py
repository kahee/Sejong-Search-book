from .base import *

secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())

DATABASES = secrets['DATABASES']

DEBUG = True
ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    '127.0.0.1',
    'localhost',
]
WSGI_APPLICATION = 'config.wsgi.production.application'
INSTALLED_APPS += [
    'django_extensions',
]

# Media(user-uploaded file)을 위한 스토리지
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'
# # Static files(collectstatic) 을 위한 스토리지
STATICFILES_STORAGE = 'config.storage.StaticFileStorage'
