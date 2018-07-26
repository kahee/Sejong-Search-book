from django.urls import path

from .views.api import keyboard, plus_friend, delete_friend, message
from .views.views import index

urlpatterns = [
    path('', index, name='index'),
    path('keyboard/', keyboard, name='keyboard'),
    path('message', message, name='message'),
    path('friend', plus_friend, name='plus-friend'),
    path('friend/<str:user_key>/', delete_friend, name='delete-firend'),
]
