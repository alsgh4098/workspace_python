from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.urls import reverse
import sqlite3

# polls 페이지 생성,
# templates에 있는 index.html을 가져와서 안에 전달해줄 인자값들을 설정해주고
# dic으로 넘겨준다.
# question변수명은 여기서 의미없다
# question 리스트로 안에 넣어준 딕셔너리들은
# 제목들과 id값들이다.
# 이렇게 만들어준 딕셔너리를 리스트에 넣어서 다시 딕셔너리(키:벨류)형태로
# index.html에 넘겨주고 이걸 렌더링한다.
# 여기서 index.html엔 별 내용이 들어있지 않지만
# 이것또한 템플릿이라고 한다.
# 정리하자면 인자값을 템플릿에 전달해주고 이걸 렌더링해준다.

def index_def(request):

    question_list = [{"id":1, "question_text":"이건제목"},
                    {"id":2, "question_text":"이건제목2"}]
    dic = {'KEY_QUESTION_LIST': question_list}
    #htmlpage = loader.get_template('polls/index.html')
    #return HttpResponse(htmlpage.render(parm_dic, request))
    return render(request, "polls/index.html", dic)



# detail.html 을 완성시켜주는 함수 detail_def


def detail_def(request, question_id):
    question_dict = {"question_text": "당신의 취미는?", "id":question_id}

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    sql = "select * from cnt1"
    cursor.execute(sql)
    cnt1 = cursor.fetchone()
    conn.close()

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    sql = "select * from cnt2"
    cursor.execute(sql)
    cnt2 = cursor.fetchone()
    conn.close()

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    sql = "select * from cnt3"
    cursor.execute(sql)
    cnt3 = cursor.fetchone()
    conn.close()

    cnt_1 = cnt1[0]

    cnt_2 = cnt2[0]

    cnt_3 = cnt3[0]

    # .1: 8000 / polls / 2 / [(0,)] / vote /

    choice_list = [{"id": 1, "choice_text" : "등산", "cnt" : cnt_1},
                   {"id": 2, "choice_text" : "낚시", "cnt" : cnt_2},
                   {"id": 3, "choice_text" : "조기축구", "cnt" : cnt_3}]
    dic = {"KEY_CHOICE_LIST" :choice_list ,'KEY_QUESTION_LIST': question_dict}
    return render(request, "polls/detail.html", dic)

def results_def(request, question_id, choice_id, cnt):
    dic={"KEY_RESULT":"차트", "cnt": cnt, "question_id" : question_id , "choice_id" : choice_id}
    return render(request, "polls/results.html",dic)


def vote_def(request, question_id, choice_id, cnt):
    cnt += 1

    if choice_id == 1:
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()
        sql = ("update cnt1 set cnt=?")
        cursor.execute(sql, (cnt,))
        conn.commit()
        conn.close()

    elif choice_id == 2:
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()
        sql = ("update cnt2 set cnt=?")
        cursor.execute(sql, (cnt,))
        conn.commit()
        conn.close()

    elif choice_id == 3:
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()
        sql = ("update cnt3 set cnt=?")
        cursor.execute(sql, (cnt,))
        conn.commit()
        conn.close()

    # sql = "update polls_question set question_text=? \
    #     where id=?"
    # cursor.execute(sql, ("왓츠뉴스", 2))
    # conn.commit()

    return HttpResponseRedirect(reverse('results_url', args=(question_id, choice_id,cnt) ))



# http://127.0.0.1:8000/polls//detail/