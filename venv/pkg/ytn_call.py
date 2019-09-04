import pkg.YTN_Craw
import pprint as p

news_list = ['https://www.ytn.co.kr/photo/photo_list_011705.html',
             'https://www.ytn.co.kr/photo/photo_list_011707.html',
            'https://www.ytn.co.kr/photo/photo_list_011706.html']

# p.pprint(news_list)
for i in news_list :
    n_list = pkg.YTN_Craw.ytn_craw(i)
    for n in n_list :
        print(n["title"])


