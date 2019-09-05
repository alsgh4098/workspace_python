
# 3과 5의 배수 구해서 다 더하기.
n = 1
sum = 0
while n <= 1000 :
    if( n % 3 == 0) :
        sum += n
    elif( n % 5 == 0) :
        sum += n
    n = n+1
print(sum)

# 게시판 페이징
# 총 페이지 수 = (총 건수 / 한 페이지당 보여 줄 건수) + 1

def getTotalPage(m,n) :
    if m % n == 0 :
        return int(m/n)
    else :
        return int((m/n) + 1)

print(getTotalPage(30,10))
print("*"*100)

class Human():
    print("응애응애")
    # 생성자 constructor __init__
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def info(self):
        print("이름 : %s 나이 : %s 성별 : %s" %(self.name, self.age, self.gender))
    def setInfo(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender
    # 소멸자
    def __del__(self):
        print("나의 죽음을 알리지 말라.")

areum = Human("minho",4,"male")

print(areum.age)
print(areum.name)
print(areum.gender)
print("*"*100)

areum.info()
areum.setInfo("areum",27,"female")
areum.info()
del areum

'''
class OMG :
    def print(print) :
        print("Oh my god")

myStock = OMG()
myStock.print()
'''


class Flight:

    def __init__(self):
        print('init')
        # 여기 __init__은 오버라이딩 되지 않은 메소드
        # flight는 상속받은 부모클래스가 없기 때문에 여기서 super는 가장 기본적인 class인 object를
        # 참조하는것.
        super().__init__()

    def __new__(cls):
        print('new')
        # 여기 __new__는 오버라이딩 되지 않은 메소드
        # flight는 상속받은 부모클래스가 없기 때문에 여기서 super는 가장 기본적인 class인 object를
        # 참조하는것.
        return super().__new__(cls)

    def number(self):
        return 'SN060'
f = Flight()
