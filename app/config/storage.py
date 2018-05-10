from storages.backends.s3boto3 import S3Boto3Storage


class StaticFilesStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class DefaultFilesStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
