from bs4 import BeautifulSoup

import requests
URL = 'https://www.melon.com/chart/'
response = requests.get(URL,headers = {"User-Agent":"XY"})
codes = response.status_code
html_text = response.text

# print(codes)
# # 결과값 200
#
# print(html_text)
# 결과값 불러온 URL의 html문 전부 출력8

# 리퀘스트로 불러온 url의 값을 beautifulsoup을 이용해서 파싱한다.
soup = BeautifulSoup(html_text, 'html.parser')

#lst50

#select는 리스트로 반환한다.
dl_list = soup.select("tr#lst50.lst50")
print(len(dl_list))

#frm > div
#frm > div
#dt > a .text 제목
#dt > a .get('href') 상세페이지주소
#dd.vertical > p > a > img 이미지
#dd.date .text
news_list = []

# dl_list는 bs클래스를 할당받은 soup에서 원하는 부분을 리스트로 파싱 받은것?
for dl in dl_list :
         # select_one은 하나의 값만 받는다.
         dic = {}
         dic["img"] = dl.select_one("div.wrap > a > img").get('src')
         dic["title"] = dl.select_one("div > div > div.ellipsis.rank01 > span > a").text
         dic["singer"] = dl.select_one("div > div > div.ellipsis.rank02 > a").text
         dic["album"] = dl.select_one("div > div > div.ellipsis.rank03 > a").text
         dic["like"] = dl.select_one("div > button >span.cnt")

         news_list.append(dic)

import pprint

pprint.pprint(news_list)