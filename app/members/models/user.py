from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from . import UserKeyword


class User(AbstractUser):
    user_key = models.CharField(
        verbose_name='user_key',
        max_length=100,
    )
    keyword = models.ForeignKey(
        UserKeyword,
        on_delete=models.CASCADE,
        related_name='user_keyword_list',
        blank=True,
        null=True,
    )
