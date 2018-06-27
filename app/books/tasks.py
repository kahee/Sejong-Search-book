import time

from .models import BookLocation, Book
from .utils import get_book_detail

from config.celery import app


__all__ = (
    'book_detail_save',
    'book_location_save',
)

# @app.task(bind=True)
# def book_detail_save(self):
#     books = Book.objects.all()
#
#     for book in books:
#         print(book.book_id)
#         if not book.ISBN:
#             get_book_detail(book.book_id)
#             print(f'{book.book_id}가 저장되었습니다.')
#     return f'끝'


@app.task()
def book_detail_save(book_id):
    get_book_detail(book_id)
    return f'{book_id}가 저장되었습니다.'


@app.task()
def book_location_save(book_id, register_id, location, book_code):
    time.sleep(3)
    book_location, _ = BookLocation.objects.update_or_create(
        register_id=register_id,
        defaults={
            'location': location,
            'book_code': book_code,
            'book': Book.objects.get(book_id=book_id),
        }
    )

    return f'{book_id}/{register_id}가 저장되었습니다.'
