import string
import requests

'''
#51~88
# 51
price = ['20180728', 100, 130, 140 , 150, 160, 170]
print(price[1:])

# 52
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])

# 53
print(nums[1::2])

# 54
nums.reverse()
print(nums)

# 55
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[::2])

# 56
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print( ''.join(interest) )

# 57
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print( '\\'.join(interest) )

# 58
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print( '\n'.join(interest) )

# 59
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)

# 60
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest = string.split('/')
print(interest)

# 62
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:2]
interest_1[0] = "Naver"
print(interest_0[:2])

# 63
# 빈 튜플생성.
my_variable = ()
print(my_variable)

# 67
# 튜플은 업데이트 안됨.
t = ('a', 'b', 'c')
print(t)
t = (t[0].upper(), t[1], t[2])
print(t)

# 68
# 튜플 -> 리스트
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)

# 69
# 리스트 -> 튜플
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)

# 70
#데이터 언패킹
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a + b + c)

# 71
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score, _, _= scores

# 72
_, _, *valid_score = scores

# 73
a, b, *valid_score = scores

# 74
temp = {}

# 75, 76
icecream = {"메로나":1000,"폴라포":1200,"빵빠레":1800}

icecream["죠스바"] = 1200 # 주의 딕셔너리에 접근할 때 대괄호로 접근

icecream["월드콘"] = 1800

# 77

print(icecream)

# 79

del icecream["메로나"]
print(icecream)

# 81

inventory = {"메로나": [300,20],"폴라포":[400,3],"빵빠레":[250,100]}

# 82

print("%d원" %inventory["메로나"][0])

# 83

print("%d개" %inventory["메로나"][1])

# 84

inventory["월드콘"] = [500,7]
print(inventory)
print('85'*100)
# 85
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream.keys())

print(icecream)
print('-'*100)
# 86
print(sum(icecream.values()))
print('-'*100)
# 87
print(icecream.values())
print(type(icecream.values()))
print('-'*100)

# 88
print('-'*100)
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
'''
# 89
# 아래 두개의 튜플을 하나의 딕셔너리로 변환하라.

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

inventory = dict(zip(keys, vals))

print(inventory)

# 90
# date와 close_price 두개의 테이블을 하나의 딕셔너리로 생성하라.
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date,close_price))

print(close_table)

# 91

print(3 == 5)

# 95
print ((3 == 3) and (4 != 3))

'''
# 101

print("입력하세요.")
string = input("입력하세요.")
for i in range(1,3) :
    print(string)


# 106
#사용자로부터 입력 받은 시간이 정각인지 판별하라.
user_in = input("현재시간:")
if user_in[3:] == "00" :
    print("정각 입니다")
else :
    print("정각이 아닙니다")


# 107

fruit = ['사과', '포도', '홍시']
user_in = input("과일을 입력해주세요.")
if(user_in in fruit) :
    print("정답입니다.")

# 110

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user_in = input("과일을 입력해주세요.")
if(user_in in fruit.values()) :
    print("정답입니다.")

# 111

user_in = input("알파벳을 입력해주세요.")
if(user_in.islower()) :
    print(user_in.upper())
else :
    print(user_in)

# 114
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

number1 = int(input("첫번째 숫자"))
number2 = int(input("두번째 숫자"))
number3 = int(input("세번째 숫자"))

max_num = max(number1,number2,number3)
print("최댓값은 %d"% max_num)



# 117

user_num = input("주민등록번호를 입력하세요.")

if(user_num[7] == ( '1' or '3')) :
    print("남자입니다.")
else :
    print("여자입니다.")
'''

# 120

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

if ( int(btc["opening_price"]) + ( int(btc["max_price"]) - int(btc["max_price"])) > int(btc["max_price"]))  :
    print("상승장")
else :
    print("하락장")


# 121

for 변수 in ["가", "나", "다", "라"]:
    print(변수)

# 122

for 변수 in ["사과", "귤", "수박"]:
    print(변수)

# 130

menu = ["면라", "밥김", "김튀"]

for food in menu :
    print(food[::-1])

# 131
# 슬라이싱

my_list = ["가", "나", "다", "라"]

print(my_list[1::])

# 132
my_list = [1,2,3,4,5,6]
print(my_list[::2])

# 134
# 역방향 출력.
my_list = ["가", "나", "다", "라"]
print(my_list[::-1])

# 135
my_list = [3, -20, -3, 44]
for i in my_list :
    if(i < 0) :
        print(i)

# 137

my_list = ["I", "study", "python", "language", "!"]

for str in my_list :
    if(len(str) >= 3 ) :
        print(str)

# 143

my_list = ["A","B","C","D"]
for al in my_list :
    if(al.islower()) :
        al.upper()
        print(al)
    else :
        al.lower()
        print(al)

# 144
file_list = ['hello.py', 'ex01.py', 'ch02.py', 'intro.hwp']

for str in file_list :
    str2 = str.split('.')
    print(str2[0])


print("-"*100)
# 145
filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']

for str in filenames :
    str2 = str.split('.')
    if (str2[1] in ('h','c')) :
        print(str)


# 149
my_list = [3,1,2,4,8,3,2,3,4,5,7]
my_list.sort()
'''
1,2,2,3,3,3,4,4,5,7,8
sole_list = []
for i in range(0,len(my_list)) :
    if(i == len(my_list)) :
        sole_list.append(my_list[i])
        continue
    elif (my_list[i] != my_list[i + 1]):
        sole_list.append(my_list[i])
        continue
print(sole_list)
'''
sole_list = []
for val in my_list :
    if val not in sole_list :
        sole_list.append(val)
print(sole_list)
