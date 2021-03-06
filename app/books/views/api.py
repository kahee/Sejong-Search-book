import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from members.models import UserKeyword
from ..utils import HELP_TEXT
from ..utils.crawling import search_book

User = get_user_model()

__all__ = (
    'keyboard',
    'message',
    'plus_friend',
    'delete_friend',
)


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'buttons': ['사용법', ]
    })


@csrf_exempt
def message(request):
    if request.method == 'POST':
        message = (request.body.decode('utf-8'))
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
            print(f'user_key: {user_key} | content: {content}')
            # 키워드가 구토인경우 특정 출판사만 출력
            if content == '구토':
                books, url = search_book('구토,문예출판사,')
            else:
                books, url = search_book(content)

            # 사용법입력이 아닌 경우에만 user_key와 검색어 User 모델에 저장
            user, _ = User.objects.get_or_create(
                username=user_key
            )

            if not url:
                wrong_keyword, _ = UserKeyword.objects.update_or_create(
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
                keyword, _ = UserKeyword.objects.update_or_create(
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
            print(f'{user_key}님이 친구추가를 하셨습니다.')
            user, _ = User.objects.update_or_create(
                username=user_key,
                defaults={
                    "is_active": True,
                }

            )
        return JsonResponse({})


@csrf_exempt
def delete_friend(request, user_key):
    if request.method == 'DELETE':
        user = User.objects.get(username=user_key)
        user.is_active = False
        user.save()
        print(f'{user_key}님이 친구삭제를 하셨습니다.')

        return JsonResponse({})
