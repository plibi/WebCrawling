import requests
from bs4 import BeautifulSoup
import datetime as dt

today = dt.datetime.today().date()

# 동행복권 당첨번호 조회페이지 url
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')


# 로또회차
round = soup.find('h4').find('strong')
# 추첨날짜
date = soup.find('p', attrs={'class':"desc"})
# 당첨번호
win_tag = soup.find('div', attrs={'class':'num win'}).find('p').find_all('span')
win_num = [num.text for num in win_tag]
# 보너스번호
bonus_num = soup.find('div', attrs={'class':'num bonus'}).find('span')

# 결과 프린트
print(f'오늘은 {today} 입니다.')
print(f'\n제 {round.text} 당첨결과 {date.text}')
print('당첨번호:', *win_num, end=' ')
print(f'+ {bonus_num.text}')


# 당첨금액, 당첨자수를 추가해줄 수도 있음
# input으로 내가 구매한 번호를 받아서 당첨확인을 해볼 수 도 있음