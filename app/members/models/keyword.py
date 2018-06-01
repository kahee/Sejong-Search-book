from django.db import models


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
