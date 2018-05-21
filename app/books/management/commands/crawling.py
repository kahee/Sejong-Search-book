import string

from django.core.management import BaseCommand

from books.utils import search_book


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('keyword', nargs='+', )

    def handle(self, *args, **options):
        keyword = options['keyword'].pop()
        result = search_book(keyword)
        result = ''.join(result)

        return result

