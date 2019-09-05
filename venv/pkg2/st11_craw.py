import requests
from bs4 import BeautifulSoup

def st_11_craw() :
    response = requests.get("http://www.11st.co.kr/html/category/1001439.html")
    codes = response.status_code
    html_text = response.content
    #받은 response에서 코드와 텍스트를 읽어서 codes html_text에 넣음.
    print(response.status_code)
    #뷰티풀숩 함수로 받아온 텍스트를 파싱해서 soup에 넣음.
    soup = BeautifulSoup(html_text, 'html.parser')
    # select는 리스트로 반환한다.

    dl_list = soup.select("#hotItem > div.viewtype > ul > li")

    item_list = []

    for dl in dl_list:
        dic = {}
        dic["href"] = dl.select_one("div > a").get('href')
        dic["img"] = dl.select_one("div > a > img").get('src')
        dic["title"] = dl.select_one("div > a > div > p").text
        dic["price"] = dl.select_one("div > a > div > div > span").text

        item_list.append(dic)

    return item_list

