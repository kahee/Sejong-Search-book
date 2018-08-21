from .base import *

DEBUG = True
ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.travis.application'
SECRET_KEY = "46sufpz*^nu$bvx!tkl45a!3#3^n83c0#8h336q@j1g7)12345",

# Test DB for Travis CI
if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'travis_ci_test',
            'USER': 'postgres',
            'PASSWORD': '',
            'PORT': 5432,
            'HOST': 'localhost',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }