import re

import requests
from bs4 import BeautifulSoup


def books_crawler(keyword):
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
    books_list = list()
    for book in body:
        for num, item in enumerate(book.contents):
            if num == 1:
                book_title = item.get_text(strip=True)
            if num == 4:
                book_info = item.strip()

        book_info = re.sub(r'/', '', book_info)
        book_status = book.find('p', class_='tag').get_text(strip=True)
        book_status = re.sub(r'\t', '', book_status)
        books_list.append(
            {
                'title': book_title,
                'info': book_info,
                'status': book_status,
            }
        )

    if not books_list:
        return '일치하는 검색 결과가 없습니다.'

    return books_list


def search_book(search):
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

    return books_crawler(keyword)


# 사용자가 입력하는 경우 '제목,출판사,저자'
# TITL,PUBN,AUTH
#
# result = keyword_split('말의품격,생능,')
# print(result)
