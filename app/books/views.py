from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['1', '2']
    })
