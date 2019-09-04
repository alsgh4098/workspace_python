from bs4 import BeautifulSoup

import requests
URL = 'https://www.ytn.co.kr/photo/photo_list_011705.html'
response = requests.get(URL)
codes = response.status_code
html_text = response.text

# print(codes)
# # 결과값 200
#
# print(html_text)
# 결과값 불러온 URL의 html문 전부 출력8

# 리퀘스트로 불러온 url의 값을 beautifulsoup을 이용해서 파싱한다.
soup = BeautifulSoup(html_text, 'html.parser')

#select는 리스트로 반환한다.
dl_list = soup.select("div#ytn_list_v2014 > dl.photo_list")
# div에 id = ytn_listv2014 아이디로 접근하고 dl에 photo_list클래스를 서낵한다.
print(len(dl_list))
# div#ytn_list_v2014 > dl.photo_list
# ytn 뉴스의 영화페이지에서 포토리스트 선택

#ytn_list_v2014 > dl:nth-child(1) > dt > a
#dt > a .text 제목
#dt > a .get('href') 상세페이지주소
#dd.vertical > p > a > img 이미지
#dd.date .text
#"https://image.ytn.co.kr/general/jpg/2019/0830/201908300953077553_k.jpg"

news_list = []

# dl_list는 bs클래스를 할당받은 soup에서 원하는 부분을 리스트로 파싱 받은것?
for dl in dl_list :
        # select_one은 하나의 값만 받는다.
        dic = {}
        dic["img"] = dl.select_one("dd.vertical > p > a > img").get('src')
        dic["title"] = dl.select_one("dt > a").text
        dic["href"] = "https:/wwww.ytn.co.kr" + dl.select_one("dt > a").get('href')
        dic["content"] = dl.select_one("dd.text > a").text
        dic["regdate"] = dl.select_one("dd.date").text

        news_list.append(dic)

if __name__ == "__main__" :
    print(news_list[0]["href"])

#pretty print
#딕셔너리 리스트를 출력해줄때 이쁘게해줌.
import pprint
pprint.pprint(news_list)