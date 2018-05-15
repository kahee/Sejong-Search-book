import requests
from bs4 import BeautifulSoup


def search_book_crawler(keyword):
    url = "http://library.sejong.ac.kr/search/Search.Result.ax"
    params = {
        'sid': 2,
        'q': keyword,
        'mf': 'true',

    }
    response = requests.get(url, params)
    print(f'url=' + response.url)
    soup = BeautifulSoup(response.text, 'lxml')

    # print(soup)


# 사용자가 입력하는 경우 '제목,출판사,저자'
# TITL,PUBN,AUTH

keyword = ''
search = ',생능,'
search_list = search.split(',')

if search_list[0] is not '':
    keyword = 'TITL:'+search_list[0]
if search_list[1] is not '':
    keyword = keyword + "|" + "PUBN:" + search_list[1]
if search_list[2] is not '':
    keyword = keyword + "|" + "AUTH:" + search_list[2]

search_book_crawler(keyword)
