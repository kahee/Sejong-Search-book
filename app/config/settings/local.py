from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'local.json'), 'rb'))
DATABASES = secrets['DATABASES']

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.local.application'

INSTALLED_APPS += [
    'django_extensions',
]

# Celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Log
LOG_DIR = os.path.join(ROOT_DIR, '.log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'django.server',
            'backupCount': 10,
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 10485760,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_error'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

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
