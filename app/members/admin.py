from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import User, UserKeyword

admin.site.register(User)
admin.site.register(UserKeyword)
