from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.urls import reverse


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

    choice_list = [{"id": 1, "choice_text" : "등산"},
                   {"id": 2, "choice_text" : "낚시"},
                   {"id": 3, "choice_text" : "조기축구"}]
    dic = {"KEY_CHOICE_LIST" :choice_list ,'KEY_QUESTION_LIST': question_dict}
    return render(request, "polls/detail.html", dic)

def results_def(request, question_id):
    dic={"KEY_RESULT":"차트"}
    return render(request, "polls/results.html",dic)

def vote_def(request, question_id):
    return HttpResponseRedirect(reverse('results_url', args=(question_id,) ))


# http://127.0.0.1:8000/polls//detail/