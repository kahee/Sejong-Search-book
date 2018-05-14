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
    message = request.body.decode('utf-8')
    return_json_str = json.loads(message)
    user_key = return_json_str['user_key']
    content = return_json_str['content']

    if content == 'test':
        response = '응답했습니다.' + user_key

    else:
        response = '해당명령어는 아직지원하지 않습니다.'

    return JsonResponse({
        "message": {
            "text": response
        }
    })
