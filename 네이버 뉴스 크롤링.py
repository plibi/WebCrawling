# 네이버 API를 이용해 원하는 키워드의 뉴스 크롤링
# Reference: https://developers.naver.com/docs/search/blog/

import requests

client_id = "f7gQygMO6hqMQ1GjdcvW"
client_secret = "LNLA1xXzPf"
headers = {'X-Naver-Client-Id':client_id,
           'X-Naver-Client-Secret':client_secret}

def get_news(keyword, start=1, display=10):
    query = keyword      
    params = {'start':start,        
              'display':display}     
    url = f"https://openapi.naver.com/v1/search/news.json?query={query}&start={params['start']}&display={params['display']}"

    request = requests.get(url, headers=headers)
    res = request.json()
    crawling = []
    for i in res['items']:
        crawling.append(i['title'])
    # print(crawling)
    # print(len(crawling))
    
    return crawling


keyword = "세계"    # 검색할 키워드 또는 topic(IT과학, 경제, 사회, 생활문화, 세계, 스포츠, 정치, 연예, 등등)
start = 1           # 검색시작지점: 1(default), 1000(max)
display = 10        # 검색건수: 10(default), 100(max)
news = get_news(keyword, start, display)
print(news)


# GET으로 json형식으로 불러와 title만 추출하는 함수
# json 결과를 확인해보면 link, description 등 더 많은 출력이 존재
# line 21~22를 수정하면 title 말고도 원하는 출력을 얻을 수 있다

## keyword가 포함된 모든 기사를 가져오는 방식인 것 같아
## 원하는 토픽의 뉴스기사를 가져오려면 다른 방법을 써야 할 것 같다