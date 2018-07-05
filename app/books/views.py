import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from members.models import UserKeyword
from .utils import HELP_TEXT, BUG_TEXT
from .utils.crawling import search_book

User = get_user_model()


def index(request):
    return HttpResponse("Wellcome")


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'buttons': ['사용법', ]
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

    # if content == '구토':
    #     return JsonResponse({
    #         'message': {
    #             'text': BUG_TEXT,
    #         },
    #     })

    else:

        user_key = return_json_str['user_key']
        print(user_key)
        books, url = search_book(content)

        # 사용법입력이 아닌 경우에만 user_key와 검색어 User 모델에 저장
        user, _ = User.objects.get_or_create(
            username=user_key
        )
        print(books)

        if not url:
            wrong_keyword, _ = UserKeyword.objects.get_or_create(
                wrong_keyword=content,
                user=user,
            )
            user.keyword = wrong_keyword
            user.save()
            return JsonResponse({
                'message': {
                    'text': books,
                },
            })
        else:
            # 검색한 키워드가 있는 경우 user키워드에 저장
            keyword, _ = UserKeyword.objects.get_or_create(
                keyword=content,
                user=user,
            )
            user.keyword = keyword
            user.save()
            print(books)
            return JsonResponse({
                'message': {
                    'text': books,
                    "message_button": {
                        'label': '자세한 검색 결과 보기',
                        'url': url,
                    }
                },
            })


@csrf_exempt
def plus_friend(request):
    if request.method == 'POST':
        request.JSON = json.loads(request.body.decode('utf-8'))
        user_key = request.JSON.get('user_key', '')
        if user_key:
            user, _ = User.objects.get_or_create(
                username=user_key
            )
        return JsonResponse({})


@csrf_exempt
def delete_friend(request, user_key):
    if request.method == 'DELETE':
        print(f'{user_key}님이 친구삭제를 하셨습니다.')

        return JsonResponse({})
