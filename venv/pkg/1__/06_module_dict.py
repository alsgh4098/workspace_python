# 06_module_dict
from functools import reduce

tup = ()
print(type(tup))
#단 튜플은 생성과 동시에 안에 값을 넣어줘야한다.

list1 = list()
print(type(list1))
#####################################################
books = dict()
books["books"] = 1000
print(books, type(books))
#####################################################
str = "{'price':1000}"
print(str, type(str))

# *arg : tuple : arguments /인자/파라미터/매개변수
# **kwargs : dict : keywards argument


# 함수  : 입력에 의해 동일한 결과를 내는 기능
# 이름(파라미터,파라미터) : print(5,'A')
# 호출 : 기존의 함수를 사용하는 것

#####################################################
#함수
def multi(a):
    i = 1
    while i <= 9:
        print (a, ' * ', i, ' = ', a * i)
        i = i + 1

print(multi(4))
#####################################################
def add(n1,n2) :
    return n1 + n2

print(add(3,8))
#####################################################
#파이썬은 함수 리턴값을 여러개 내보낼 수 있다.
#다른 언어에서는 안됨.
#타입이 같을 필요도 없음.
print("*"*100)
def add(n1,n2) :
    res1 = n1 + n2
    res2 = n1 * n2
    res3 = "ABC"
    return res1,res2,res3

(r1,r2,r3) = add(1,2)

print(r1,r2,r3)
print(add(1,2))

print("*"*100)
#####################################################
def listPrint(num, *book_list) :
    print(book_list)

listPrint(1,2,3,4,5)
#튜플은 모든 파라미터 뒤에 둬야된다.

print("*"*100)
#####################################################

def dicPrint(**dic) :
    print(dic)

aa = {"uid":"kim","upw":"111"}

dicPrint(uid = "kim",upw = "111")
#dicPrint(aa) # error
# dict타입을 key = "" 로 전달해야한다.
print("*"*100)
'''
#####################################################
def dicPrint(**dic) :
    print(self)


bb = dict(uid = "kim",upw = "111")
print(bb)
dicPrint(bb) # error

print("*"*100)
#####################################################
'''
def tpl_dic_Print(*t,**d) :
    print(t,d)
tpl_dic_Print([1,2,3], uid = "kim",upw = "111")

print("*"*100)
#####################################################

def tpl_dic_Print(str, *t, **d) :
    print(str, t, d)

tpl_dic_Print("aa", 0, 1,2,3, uid = "kim",upw = "111")

help(print)

'''
#람다
print((lambda x,y: x + y)(10,20))

#맵
print(list2)
print(list(map(lambda x: x ** 2, range(5))))
# 캐스팅이 필요하다.
list2 = list( map(lambda x: x ** 2, range(5)) )


####################################################
#리듀스

print( reduce( lambda x, y: x + y, [0, 1, 2, 3, 4]) )

####################################################
#필터

