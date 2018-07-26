from django.http import HttpResponse

__all__ = (
    'index',
)


def index(request):
    return HttpResponse("Wellcome")
