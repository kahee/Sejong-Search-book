import json

from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def keyboard(request):
    return JsonResponse({
        'type': 'text',
        'buttons': ['1', '2']
    })


@csrf_exempt
def message(request):
    if request.method == 'POST':
        message = ((request.body).decode('utf-8'))
        print(request.body)
        return_json_str = json.loads(message)
        return_str = return_json_str['content']

        return JsonResponse({
            'message': {
                'text': "you type " + return_str + "!"
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['1', '2']
            }
        })

# def keyboard(request):
#     return JsonResponse({
#         'type': 'text',
#         'buttons': ['test', '2']
#     })
#
#
# @csrf_exempt
# def search_book(request):
#     message = ((request.body).decode('utf-8'))
#     return_json_str = json.loads(message)
#     return_str = return_json_str['content']
#
#     return JsonResponse({
#         'message': {
#             'text': "you type " + return_str + "!"
#         },
#         'keyboard': {
#             'type': 'buttons',
#             'buttons': ['1', '2']
#         }
#     })
#
#     # message = request.body.decode('utf-8')
#     # return_json_str = json.loads(message)
#     # user_key = return_json_str['user_key']
#     # content = return_json_str['content']
#     #
#     # if content == 'test':
#     #     response = '응답했습니다.' + user_key
#     #
#     # else:
#     #     response = '해당명령어는 아직지원하지 않습니다.'+ user_key
#     #
#     # return JsonResponse({
#     #     "message": {
#     #         "text": response
#     #     }
#     # })
