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

    content = return_json_str['content']
    user = return_json_str['user_key']
    books = search_book(content)
    print(books)

    return JsonResponse({
        'message': {
            'text': books,
        },
    })
