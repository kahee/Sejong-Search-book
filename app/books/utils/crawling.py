import re
import requests
from bs4 import BeautifulSoup

from ..models import Book


__all__ = (
    'get_book_detail',
    'get_book_location',
    'get_book_lists',
    'search_book_title',
    'search_book_detail',
    'search_book',
)


def get_book_detail(book_id):
    """
    책 상세 정보를 크롤링하는 함수
    :param book_id:
    :return:
    """
    url = "http://library.sejong.ac.kr/search/DetailView.ax"
    params = {
        'sid': 2,
        'cid': book_id
    }

    response = requests.get(url, params)
    soup = BeautifulSoup(response.text, 'lxml')
    contents = soup.find('div', class_='contents')

    meta_data_body = contents.find('tbody', id='metaDataBody').find_all('td')
    items = [item.get_text(strip=True).replace(' :', '') for item in meta_data_body]
    td = iter(items)
    book_info_dict = dict(zip(td, td))

    # book상세 정보 DB에 저장
    book_info, _ = Book.objects.update_or_create(
        book_id=book_id,
        defaults={
            "book_type": book_info_dict.get('자료유형', ' '),
            "book_author": book_info_dict.get('서명 / 저자', ' '),
            "book_personnel_author": book_info_dict.get('개인저자', ' '),
            "book_issue": book_info_dict.get('발행사항', ' '),
            "book_form": book_info_dict.get('형태사항', ' '),
            "ISBN": book_info_dict.get('ISBN', ' '),
        }
    )

    return book_info


def get_book_location(book_id, book_info=None):
    """
    도서 위치 및 대출 정보를 크롤링하는 함수
    book_info = 해당 boook_id를 가진 Book모델 객체
    :param book_id:
    :param book_info:
    :return: 서가위치, 도서번호, 대출여부
    """
    """
    
    """
    post_format = {
        'cid': book_id,
    }

    r = requests.post('http://library.sejong.ac.kr/search/ItemDetailSimple.axa', data=post_format)
    test = BeautifulSoup(r.content, 'html.parser')
    tbody = test.find('tbody').find_all('tr')

    # book_list = ['제1자료실(5층)', '658.31125 한17공3', '대출가능'] 정보 가진 리스트
    books_list = list()
    for item in tbody:
        td = item.find_all('td')

        # location_list = ['000000911692', '제2자료실(6층)', '811.4 이19말', '대출가능']
        # book = ['제2자료실(6층)', '811.4 이19말', '대출가능']
        # book_info = Book 모델 객체 (해당 book_id를 가진 모델)
        book = list()
        location_list = list()
        for num, td_item in enumerate(td):
            if num is 0:
                # ['000000572988']
                location_list.append(td_item.get_text(strip=True))
            if num in range(1, 4):
                location_list.append(td_item.get_text(strip=True))
                book.append(td_item.get_text(strip=True))

        # BookLocation 모델 생성
        register_id = location_list[0]
        location = location_list[1]
        book_code = location_list[2]
        from books import tasks
        tasks.book_location_save.delay(book_id, register_id, location, book_code)

        # book_location, _ = BookLocation.objects.update_or_create(
        #     register_id=location_list[0],
        #     defaults={
        #         'location': location_list[1],
        #         'book_code': location_list[2],
        #         'book': Book.objects.get(book_id=book_id),
        #     }
        # )

        books_list.append(book)

    return books_list


def get_book_lists(keyword):
    """
    세종대학교 학술정보원 사이트에서 해당 keyword 정보 크롤링

    :param keyword:
    :return: title/info/status
    """
    url = "http://library.sejong.ac.kr/search/Search.Result.ax"
    params = {
        'sid': 2,
        'q': keyword,
        'mf': 'true',
    }

    response = requests.get(url, params)
    soup = BeautifulSoup(response.text, 'lxml')
    body = soup.find('ul', class_='listType01').find_all('div', class_='body')

    books = ''
    if body:
        # 검색한 키워드의 결과가 있는 경우
        for book in body:
            book_numbers = book.find('a', class_='title', href=True)['href']
            p = re.compile(r'javascript:search.goDetail[(](\d+)[)]')
            book_id = p.search(book_numbers).group(1)

            book_instance, _ = Book.objects.get_or_create(
                book_id=book_id,
            )

            # 도서 상세 정보 저장 -> celery 로 실행
            from books import tasks
            tasks.book_detail_save.delay(book_id)

            # 도서 위치 및 대출 여부
            # locations = ['제1자료실(5층)', '658.31125 한17공3', '대출가능']
            locations = get_book_location(book_id)

            books_status = ''
            for items in locations:
                # 도서 위치 string으로 변환
                # books_status = 보존서고10층A(9층문의), 658.01 공19ㅅ, 대출불가
                books_status = books_status + ', '.join(str(item) for item in items) + '\n'

            for num, item in enumerate(book.contents):
                # 책 제목
                if num == 1:
                    book_title = item.get_text(strip=True)
                # 책 저자/출판정보
                if num == 4:
                    # book_info_result = / 송대희. 한국개발연구원 , 1987.
                    book_info_result = item.strip()
            book_info_result = re.sub(r'/', '', book_info_result)

            books = books + book_title + "\n" + book_info_result + "\n" + books_status + "---------" + "\n"
        return books, response.url

    # 검색한 키워드 결과가 없는 경우
    if not body:
        books = '검색하신 결과가 없습니다.\n 사용법을 알고 싶으시면 "사용법"을 입력해주세요'
        url = None
        return books, url


def search_book_title(search):
    """
    제목을 통한 도서 검색 키워드 생성
    :param search:
    :return:
    """
    keyword = 'TITL:' + search
    return get_book_lists(keyword)


def search_book_detail(search):
    """
    사용자가 search('제목,출판사,저자')를 입력하면 항목에 따라
    keyword를 생성후 크롤링 함수 실행

    :param search:
    :return: search에 입력한 책 정보 출력
    """
    keyword = ''
    search_list = search.split(',')

    if search_list[0] is not '':
        keyword = 'TITL:' + search_list[0]
    if search_list[1] is not '':
        keyword = keyword + "|" + "PUBN:" + search_list[1]
    if search_list[2] is not '':
        keyword = keyword + "|" + "AUTH:" + search_list[2]

    return get_book_lists(keyword)


def search_book(keyword):
    if keyword.count(',') is 2:
        return search_book_detail(keyword)

    else:
        return search_book_title(keyword)

# # 사용자가 입력하는 경우 '제목,출판사,저자'
# # TITL,PUBN,AUTH
# result = search_book('컴퓨터구조론,생능,')
# print(result)
# get_book_detail(1578922)
# book_location(1578922)
