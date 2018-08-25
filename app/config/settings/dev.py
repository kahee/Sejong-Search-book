from .base import *

# AWS
AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = SECRETS['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = SECRETS['AWS_S3_REGION_NAME']
AWS_S3_SIGNATURE_VERSION = SECRETS['AWS_S3_SIGNATURE_VERSION']
AWS_DEFAULT_ACL = SECRETS['AWS_DEFAULT_ACL']

secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json'), 'rb'))
DATABASES = secrets['DATABASES']

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
