import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    last_visit = models.DateTimeField(auto_now=True)

