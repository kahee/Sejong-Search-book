from django.urls import path
from books import views

urlpatterns = [
    path('keyboard/', views.keyboard, name='keyboard'),
    path('message', views.message, name='message'),
    path('friend', views.plus_friend, name='plus-friend'),
    path('friend/<str:user_key>/', views.delete_friend, name='delete-firend'),
]
