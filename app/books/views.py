import json
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from books.utils import HELP_TEXT
from books.utils.crawling import search_book


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'buttons': ['1', '2']
    })


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)

    content = return_json_str['content']

    if content == '도움말':
        return JsonResponse({
                'message': {
                    'text': HELP_TEXT,
                },
            })

    else:
        user = return_json_str['user_key']
        books, url = search_book(content)
        if not url:
            return JsonResponse({
                'message': {
                    'text': books,
                },
            })

        return JsonResponse({
            'message': {
                'text': books,
                "message_button": {
                    'label': '자세한 검색 결과 보기',
                    'url': url,
                }
            },
        })
