from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from config import settings

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username=settings.SECRETS['SUPERUSER_USERNAME']).exists():
            User.objects.create_superuser(
                username=settings.SECRETS['SUPERUSER_USERNAME'],
                password=settings.SECRETS['SUPERUSER_PASSWORD'],
                email=settings.SECRETS['SUPERUSER_EMAIL'],
            )
