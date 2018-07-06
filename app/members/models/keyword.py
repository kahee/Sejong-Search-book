from django.conf import settings
from django.db import models
from django.utils import timezone


class UserKeyword(models.Model):
    keyword = models.CharField(
        verbose_name='검색키워드',
        max_length=255,
        blank=True,
        null=True,
    )
    wrong_keyword = models.CharField(
        verbose_name='찾지 못한 키워드',
        max_length=255,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_keyword_list',
        blank=True,
        null=True,
    )
    creation_datetime = models.DateTimeField('생성시간', auto_now=True)

    def __str__(self):
        return self.keyword
