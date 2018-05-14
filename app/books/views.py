import json

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['1', '2']
    })


def search_book(request):
    if request.method == 'POST':
        request.JSON = json.loads(request.body.decode('utf-8'))

    else:
        request.JSON = {}

    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']

    if content.startwith('test'):
        response = '응답했습니다.'

    else:
        response = '해당명령어는 아직지원하지 않습니다.'

    return {
        'message': {
            'text': response
        }
    }
