import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from members.models import UserKeyword
from .utils import HELP_TEXT
from .utils.crawling import search_book

User = get_user_model()


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'buttons': ['사용법',]
    })


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    content = return_json_str['content']

    if content == '사용법':
        return JsonResponse({
            'message': {
                'text': HELP_TEXT,
            },
        })

    else:
        user_key = return_json_str['user_key']
        books, url = search_book(content)

        # 사용법입력이 아닌 경우에만 user_key와 검색어 User 모델에 저장
        user, _ = User.objects.get_or_create(
            username=user_key
        )
        keyword, _ = UserKeyword.objects.get_or_create(
            keyword=content,
        )
        user.keyword = keyword
        user.save()

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
