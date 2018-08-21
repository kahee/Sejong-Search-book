
DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.travis.application'

# Test DB for Travis CI
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

