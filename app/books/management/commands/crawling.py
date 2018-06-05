from django.core.management import BaseCommand
from books.utils import search_book


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('keyword', nargs='+', )

    def handle(self, *args, **options):
        keyword = options['keyword'].pop()
        result, url = search_book(keyword)

        return result
