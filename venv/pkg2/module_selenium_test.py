from selenium import webdriver
#웹드라이버를 이용하면 크롬부라우저를 이용할 수 있다.
from bs4 import BeautifulSoup

from webdriver_manager.chrome import ChromeDriverManager
def sti_11craw(prm_search_str) :
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://front.wemakeprice.com/category/division/2100132")
    serch_box = driver.find_element_by_name("search_keyword")
    serch_box.send_keys(prm_search_str)

    search_button = driver.find_element_by_id("_searchKeywordBtn")
    search_button.click()

    html_text = driver.page_source
    soup = BeautifulSoup(html_text, 'html.parser')

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
        print(dl)
        for i in range(1, 10):
            dic = {}
            dic["href"] = dl.select_one("a:nth-child(%d)" % i).get('href')
            dic["img"] = dl.select_one("a:nth-child(%d) > div > div.item_img > img" % i).get('data-lazy-src')
            dic["title"] = dl.select_one("a:nth-child(%d) > div > div.item_cont > div.option_txt > p" % i).text
            dic["price"] = dl.select_one(
                "a:nth-child(%d) > div > div.item_cont > div.option_txt > div > div.price_info > strong > em" % i).text
            dic["sold"] = dl.select_one(
                "a:nth-child(%d) > div > div.item_cont > div.option_txt > div > div.price_info > span > span.num" % i).text.replace(
                "\n                              ", "", 1)
            i += 1
            item_list.append(dic)
            

if __name__ == "__main__" :
    sti_11craw("삼성")