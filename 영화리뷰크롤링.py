import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver'
keyword = '무역전쟁'    # 찾고싶은 키워드
params = {
    'where': 'news',
    'query': keyword}

res = requests.get(url, params=params)
print(res.status_code)
# print(dir(res))
# ['apparent_encoding', 'close', 'connection', 'content', 'cookies',
#  'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect',
#  'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 
#  'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 
#  'text', 'url']
# print(res.text)

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.prettify())  # 예쁘게 보이기

sample = soup.select('#sp_nws1 > div.news_wrap.api_ani_send > div > a.title')
print(len(sample))
print(sample)