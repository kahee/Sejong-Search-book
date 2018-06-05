from django.db import models

from . import Book


class BookLocation(models.Model):
    register_id = models.CharField(
        verbose_name='등록번호',
        unique=True,
        max_length=100,
    )

    location = models.CharField(
        verbose_name='소장위치',
        blank=True,
        max_length=100,
    )
    book_code = models.CharField(
        verbose_name='청구기호',
        max_length=255,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='book_location_list',
        null=True,
    )
