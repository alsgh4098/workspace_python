import requests
from bs4 import BeautifulSoup


def WMP_craw() :
    response = requests.get("https://front.wemakeprice.com/category/division/2100132")
    codes = response.status_code
    html_text = response.text
    #받은 response에서 코드와 텍스트를 읽어서 codes html_text에 넣음.
    print(response.status_code)
    #뷰티풀숩 함수로 받아온 텍스트를 파싱해서 soup에 넣음.
    soup = BeautifulSoup(html_text, 'html.parser')

    # select는 리스트로 반환한다.
    dl_list = soup.select("#list_lists > div")

    item_list = []

    # 이미지 : #list_lists > div > a:nth-child(1) > div > div.item_img > img
    # 이름 : list_lists > div > a:nth-child(1) > div > div.item_cont > div.option_txt > p
    # 가격 : list_lists > div > a:nth-child(1) > div > div.item_cont > div.option_txt > div > div.price_info > strong > em
    # 구매횟수 : list_lists > div > a:nth-child(1) > div > div.item_cont > div.option_txt > div > div.price_info > span > span.num
    # 링크 : #list_lists > div > a:nth-child(1) > a

    # dl_list는 bs클래스를 할당받은 soup에서 원하는 부분을 리스트로 파싱 받은것?
    for dl in dl_list:
        # select_one은 하나의 값만 받는다.

        for i in range(1,10) :
            dic = {}
            dic["href"] = dl.select_one("a:nth-child(%d)" %i).get('href')
            dic["img"] = dl.select_one("a:nth-child(%d) > div > div.item_img > img" %i).get('data-lazy-src')
            dic["title"] = dl.select_one("a:nth-child(%d) > div > div.item_cont > div.option_txt > p"%i ).text
            dic["price"] = dl.select_one("a:nth-child(%d) > div > div.item_cont > div.option_txt > div > div.price_info > strong > em"%i).text
            dic["sold"] = dl.select_one("a:nth-child(%d) > div > div.item_cont > div.option_txt > div > div.price_info > span > span.num"%i).text.replace("\n                              ","",1)
            i += 1
            item_list.append(dic)


    return item_list

