# class
'''
#누적해서 입력받은 값을 더하는 함수.
result = 0

def add(num) :
    global result
    result += num
    return result

print(add(3))
print(add(4))
print(add(38))

'''

#위에 누적해서 더해주는 add 기능을 두번 사용하고 싶다 하면
#함수를 두번 생성하고, 전역변수를 두번 생성해야하는 낭비, 번거로움이 있다.

class adder:
    #인스턴스 생성시 초기에 변수를 지정해주는 메소드
    def __init__(self) :
        self.result = 0
    def add(self, num) :
        self.result += num
        return self.result

cal1 = adder()
cal2 = adder()

print(cal1.add(3))
print(cal1.add(5))
print(cal1.add(13))
print(cal1.add(23))
print("*"*100)
print(cal2.add(8))
print(cal2.add(7))
print(cal2.add(2))
print(cal2.add(1))