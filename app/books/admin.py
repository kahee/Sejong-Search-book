from django.contrib import admin

# Register your models here.
from .models import Book, BookLocation

admin.site.register(Book)
admin.site.register(BookLocation)
