import json
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from crawling import search_book


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'buttons': ['1', '2']
    })


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)

    if not return_json_str['content']:
        books = '검색어를 입력해주세요\n' + '도서명,출판사,저자\n' + 'ex) 컴퓨터구로존,생능,'

    else:
        content = return_json_str['content']
        user = return_json_str['user_key']
        books = search_book(content)

    return JsonResponse({
        'message': {
            'text': books,
        },
    })

