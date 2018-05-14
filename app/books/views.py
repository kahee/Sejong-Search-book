import json

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'buttons': ['test', '2']
    })


@csrf_exempt
def search_book(request):
    if request.method == 'POST':
        request.JSON = json.loads(request.body.decode('utf-8'))

    else:
        request.JSON = {}

    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']

    if content.startwith('test'):
        response = '응답했습니다.'+user_key+''+type

    else:
        response = '해당명령어는 아직지원하지 않습니다.'

    return JsonResponse({
        'message': {
            'text': response
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['Tron', 'Bitcoin', 'ADA']
        }

    })
