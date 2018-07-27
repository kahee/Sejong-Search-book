from django.urls import path


from ..views.views import index

urlpatterns = [
    path('', index, name='index'),
]
