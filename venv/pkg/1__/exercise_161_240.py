# 171~180

class myInt() :
    def __init__(self,number):
        self.number = number

    def __add__(self, other) :
        self.number += other

    def num(self) :
        print(self.number)

    def print(self):
        print(self.number)

l = myInt(4)
r = myInt(3)

l.__add__(3)

l.num()
l.print()
#이상함


# 클래스를 상속받으면 상속받은 클래스의 변수도 상속받는데, 변수명이 같을경우 변수의 우선순위가 있다
# 같은 이름의 메소드를 상속받았을경우 메소드 우선순위가 있는것과 같다.
class A :
    number = 3
    def num1(self) :
        print(self.number)

class B :
    number3 = 9
    def num3(self) :
        print(self.number3)

class C(A,B) :
    def study(self) :
        print("공부하기")

testC = C()

testC.num1()
testC.num3()
testC.study()


# class Person:
#     def greeting(self):
#         print('안녕하세요.')
#
#
# class University:
#     def manage_credit(self):
#         print('학점 관리')
#
#
# class Undergraduate(Person, University):
#     def study(self):
#         print('공부하기')
#
# james = Undergraduate()
# james.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
# james.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
# james.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드