import os

SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')
if not SETTINGS_MODULE or SETTINGS_MODULE == 'config.settings':
    from .local import *

if SETTINGS_MODULE is not 'config.settings.travis':
    from .base import *
    SECRETS_DIR = os.path.join(ROOT_DIR, '.secrets')
    SECRETS_BASE = os.path.join(SECRETS_DIR, 'base.json')
    secrets = json.loads(open(SECRETS_BASE, 'rt').read())
    SECRET_KEY = secrets['SECRET_KEY']

    # AWS
    AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_REGION_NAME = secrets['AWS_S3_REGION_NAME']
    AWS_S3_SIGNATURE_VERSION = secrets['AWS_S3_SIGNATURE_VERSION']
    AWS_DEFAULT_ACL = secrets['AWS_DEFAULT_ACL']
    AWS_ELASTIC_CACHE = secrets['AWS_ELASTIC_CACHE']

    # CREATE SUPER USER
    SUPERUSER_USERNAME = secrets['SUPERUSER_USERNAME']
    SUPERUSER_PASSWORD = secrets['SUPERUSER_PASSWORD']
    SUPERUSER_EMAIL = secrets['SUPERUSER_EMAIL']
