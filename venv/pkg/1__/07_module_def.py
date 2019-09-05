from functools import reduce
import math
# 내장 패키지

# 06_module_def
''' *arg **keyarg 가변인자 이해
def listPrint(num,*book_list) :
    print(num , book_list)
listPrint(1,2,3,4,5,6,7,8)

print("*"*100)

def listPrint(*book_list) :
    print(book_list)
listPrint("Aaaa","bbbb")

print("*"*100)
# positional arguments
# keyword arguments

def save_ranking(first, second, third=None, fourth=None):
    rank = {}
    rank[1], rank[2] = first, second
    rank[3] = third if third is not None else 'Nobody'
    rank[4] = fourth if fourth is not None else 'Nobody'
    print(rank)

# positional arguments 2개 전달
save_ranking('ming', 'alice')
# positional arguments 2개와 keyword argument 1개 전달
save_ranking('alice', 'ming', fourth='jim')
# positional arguments 2개와 keyword arguments 2개 전달 (단, 하나는 positional argument 형태로 전달)
save_ranking('alice', 'ming', 'mike', fourth='jim')
'''
'''
#함수이름 : login
#파라미터 : id, pw
#결괄리턴 : 홍길동

def login(id,pw) :
    return "홍길동"

print(login('jin','123'))

#함수이름 : maxmin
#파라미터 : 리스트
#결괄리턴 : max, min

def maxmin(list) :
    max1 = max(list)
    min1 = min(list)
    return (max1,min1)

list = [4,46,4,2,45,6,7,1,3,4,16,45,12,43,6,7,8,56,4,3]

print(maxmin(list))
'''
'''

#함수이름 : bmi
#파라미터 : height, weight
#결괄리턴 : bmi수치

def bmi(weight, height) :
    height2 = height/100
    bmi_n = (weight / ((height2)*(height2)))
    print(round(bmi_n,2))
    if(bmi_n < 18.5) :
        bmi_str = "마름"
    elif(18.5 <= bmi_n and bmi_n < 25.0) :
        bmi_str = "보통"
    elif (25.0 <= bmi_n and bmi_n < 30.0):
        bmi_str = "비만"
    elif (30.0 <= bmi_n < 70.0):
        bmi_str = "고도비만"
    else :
        bmi_str = "수치이상"
    return bmi_str

print( bmi(72, 181) )

# 재귀함수
def countdown(n) :
    if n == 0 :
        print("blastoff!")
    else :
        print("%d..!"%n)
        countdown(n-1)

countdown(3)


# * 가변인자 사용.
# 받은 인자들은 튜플에 담김.

def bmi(*args) :
    height = args[1]
    print(height)
    weight = args[0]
    print(weight)
    height2 = height/100
    bmi_n = (weight / ((height2)*(height2)))
    print(round(bmi_n,2))
    if(bmi_n < 18.5) :
        bmi_str = "마름"
    elif(18.5 <= bmi_n and bmi_n < 25.0) :
        bmi_str = "보통"
    elif (25.0 <= bmi_n and bmi_n < 30.0):
        bmi_str = "비만"
    elif (30.0 <= bmi_n < 70.0):
        bmi_str = "고도비만"
    else :
        bmi_str = "수치이상"
    return bmi_str

print( bmi(72, 181) )
'''

'''
# **가변인자 사용.(key값 사용.)
def bmi(**Kargs) :
    height = Kargs["height"]
    print("입력받은 키 %d"%height)
    weight = Kargs['weight']
    print("입력받은 몸무게 %d"%weight)
    height2 = height/100
    bmi_n = (weight / ((height2)*(height2)))
    print("bmi 수치 : %d" %round(bmi_n,2))
    if(bmi_n < 18.5) :
        bmi_str = "마름"
    elif(18.5 <= bmi_n and bmi_n < 25.0) :
        bmi_str = "보통"
    elif (25.0 <= bmi_n and bmi_n < 30.0):
        bmi_str = "비만"
    elif (30.0 <= bmi_n < 70.0):
        bmi_str = "고도비만"
    else :
        bmi_str = "수치이상"
    return bmi_str

print( "비만도 : " ,bmi( weight = 72, height = 181) )

'''
'''
# 함수이름 : circle
# 파라미터 : r
# 결과리턴 : areas (PI*r*r) (2*PI*r)

def circle(r) :
    return (round(3.14*r*r , 2), round(2*3.14*r , 2))

print( "넓이 : %d 둘레 : %d" % circle(int(input("반지름을 입력해주세요."))) )
'''
'''
#math 패키지 사용.
def circle(r) :
    area = round(math.pi * r**2,2)
    circum = round(math.pi * r *2,2)
    return (area,circum)

print(pow(2,4))
print(math.pow(2,4))
print(math.pi)
print(circle(5))

print( pow(3,3,2) )
# 3의 3승을 2로 나눈 나머지
'''
'''
#주소값 확인.
list = [1,2,3,5,6,7]
print(id(list))
# unpacking
'''
# Unpacking
# 컨테이너 타입에 *을 붙이면 언패킹이 된다.
primes = [2, 3, 5, 7, 11, 13]

# *numbers의 의미는 가변인자로 갯수제한 없이 numbers에 받아서 튜플에 넣겠다.
def product(*numbers):
    p = reduce(lambda x, y : x * y, numbers)
    return p

# *primes의 의미는 primes 리스트속 안으로 접근([]안으로, 언패킹)
print(product(*primes))

# primes 리스트 그대로
print(product(primes))

# primes 리스트속 안으로 접근([]안으로, 언패킹)
print(*primes)

# primes 리스트 그대로
print(primes)
'''
headers = {
    'Accept': 'text/plain',
    'Content-Length': 348,
    'Host': 'http://mingrammer.com'
}

def pre_process(**headers):
    content_length = headers['Content-Length']
    print('content length: ', content_length)

    host = headers['Host']
    if 'https' not in host:
        raise ValueError('You must use SSL for http communication')

pre_process(**headers)
'''
