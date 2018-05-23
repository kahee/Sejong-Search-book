from django.db import models

from . import BookLocation


class Book(models.Model):
    """
    book_id, 자료유형, 서명/저자, 개인저자, 발행사항, 형태사항, ISBN, 청구기호 , location(Foreign)
    """
    book_id = models.CharField(
        verbose_name='book_id',
        max_length=100,
    )
    book_type = models.CharField(
        verbose_name='자료유형',
        max_length=255,
        blank=True,
    )
    book_author = models.CharField(
        verbose_name='서명/저자',
        max_length=255,
        blank=True,
    )
    book_personnel_author = models.CharField(
        verbose_name='개인저자',
        max_length=255,
        blank=True,
    )
    book_issue = models.CharField(
        verbose_name='발행사항',
        max_length=255,
        blank=True,
    )
    book_form = models.CharField(
        verbose_name='형태사항',
        max_length=255,
        blank=True,
    )
    ISBN = models.CharField(
        verbose_name='ISBN',
        max_length=255,
        blank=True,
    )
    book_location = models.ForeignKey(
        BookLocation,
        on_delete=models.CASCADE,
        related_name='book_location_list',
        null=True,
    )
