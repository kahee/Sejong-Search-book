# Generated by Django 2.0.5 on 2018-07-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20180702_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.TextField(blank=True, verbose_name='서명/저자'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_form',
            field=models.TextField(blank=True, verbose_name='형태사항'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_issue',
            field=models.TextField(blank=True, verbose_name='발행사항'),
        ),
    ]