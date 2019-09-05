'''
def dicPrint(**dic) :
    print(dic)
# **dic은 파라미터 dic으로 가변인자(갯수제한없이)를 받아서 딕셔너리에 전부 넣겠다는 의미다.

aa = {"uid":"kim","upw":"111"}

# 기존의 딕셔너리를 넣기위해서는 딕셔너리 언패킹 **을 붙여서 넣어준다.
dicPrint(**aa)

# 새로운 딕셔너리를 인자로 넣어주기 위해서는 우리가 알고있던 딕셔너리 형태와 다르게 입력해줘야 한다.
# **면

dicPrint(**{"uid":"kim","upw":"111"})


dicPrint(uid = "kim",upw = "111")

# dicPrint(aa) # error
# dict타입을 key = "" 로 전달해야한다.
'''

def tpl_dic_Print(str, *t, **d) :
    print(str, t, d)

tpl_dic_Print("aa", 0, 1,2,3, uid = "kim",upw = "111")