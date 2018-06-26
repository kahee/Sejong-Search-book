from .models import Book
from .utils import get_book_detail
from config.celery import app


@app.task(bind=True)
def book_detail_save(self):
    books = Book.objects.all()

    for book in books:
        print(book.book_id)
        if not book.ISBN:
            get_book_detail(book.book_id)
            print(f'{book.book_id}가 저장되었습니다.')
    return f'끝'
