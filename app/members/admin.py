from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserKeyword


class UserAdmin(BaseUserAdmin):
    readonly_fields = ('last_visit',)
    list_display = ('username', 'last_visit', 'is_active', 'is_staff')
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            ),
        }),
        ('개인정보', {
            'fields': (
                'last_name',
                'first_name',
            ),
        }),
        ('권한', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
        ('주요 일자', {
            'fields': (
                'last_visit',
                'last_login',
                'date_joined',
            ),
        }),
    )


class UserKeywordAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_datetime',)
    list_display = ('user', 'keyword', 'wrong_keyword',)


admin.site.register(User, UserAdmin)
admin.site.register(UserKeyword, UserKeywordAdmin)
