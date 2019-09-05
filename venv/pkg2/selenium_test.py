from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pprint as p
# 셀레니움 + 뷰티풀숩

def WMP_Sel_Craw(str) :
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://front.wemakeprice.com/category/division/2100132")
    serch_box = driver.find_element_by_name("search_keyword")
    serch_box.send_keys(str)

    search_button = driver.find_element_by_id("_searchKeywordBtn")
    search_button.click()

    html_text = driver.page_source


    soup = BeautifulSoup(html_text, 'html.parser')
    dl_list = soup.select("#_contents > div.content_main > div.search_wrap > div:nth-child(4) > div.box_listwrap.tab_cont > div > a")

    item_list = []


    for dl in dl_list:
        # select_one은 하나의 값만 받는다.
        # _contents > div.content_main > div.search_wrap > div:nth-child(4) > div.box_listwrap.tab_cont > div > a:nth-child(1) >
        dic = {}
        dic["href"] = dl.get('href')
        dic["img"] = dl.select_one(" div > div.item_img > img").get("data-lazy-src")
        dic["title"] = dl.select_one("div > div.item_cont > div.option_txt > p").text
        dic["price"] = dl.select_one("div > div.item_cont > div.option_txt > div > div.price_info > strong > em").text
        # dic["sold"] = dl.select_one("div > div.item_cont > div.option_txt > div > div.price_info > span > span.num").text.replace("\n                              ", "", 1)
        item_list.append(dic)

    # p.pprint(item_list)

    return item_list