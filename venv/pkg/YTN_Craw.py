from bs4 import BeautifulSoup
import requests
# request는 인터넷 연결을 요청해주는 함수?

#입력받은 url에 request함수로 연결해서 response에 받음.
def ytn_craw(URL) :
    response = requests.get(URL)
    codes = response.status_code
    html_text = response.text
    #받은 response에서 코드와 텍스트를 읽어서 codes html_text에 넣음.

    #뷰티풀숩 함수로 받아온 텍스트를 파싱해서 soup에 넣음.
    soup = BeautifulSoup(html_text, 'html.parser')



    # select는 리스트로 반환한다.
    dl_list = soup.select("div#ytn_list_v2014 > dl.photo_list")
    # div에 id = ytn_listv2014 아이디로 접근하고 dl에 photo_list클래스를 한다.
    # div#ytn_list_v2014 > dl.photo_list
    # ytn 뉴스의 영화페이지에서 포토리스트 선택

    # ytn_list_v2014 > dl:nth-child(1) > dt > a
    # dt > a .text 제목
    # dt > a .get('href') 상세페이지주소
    # dd.vertical > p > a > img 이미지
    # dd.date .text
    # "https://image.ytn.co.kr/general/jpg/2019/0830/201908300953077553_k.jpg"

    news_list = []

    # dl_list는 bs클래스를 할당받은 soup에서 원하는 부분을 리스트로 파싱 받은것?
    for dl in dl_list:
        # select_one은 하나의 값만 받는다.
        href = dl.select_one("dt > a").get('href')
        dic = {}
        dic["img"] = dl.select_one("dd.vertical > p > a > img").get('src')
        dic["title"] = dl.select_one("dt > a").text
        dic["href"] = "https:/www.ytn.co.kr" + href
        dic["content"] = dl.select_one("dd.text > a").text
        dic["regdate"] = dl.select_one("dd.date").text
        #포토리스트를 이미지 타이틀 링크 내용 데이터를 dic형태로 만들어서 news_list에 넣어줌.

        news_list.append(dic)

        print(news_list)

    # pretty print
    # 딕셔너리 리스트를 출력해줄때 이쁘게해줌.
    return news_list

# if __name__ == "__main__":
#     news_list = ytn_craw()
