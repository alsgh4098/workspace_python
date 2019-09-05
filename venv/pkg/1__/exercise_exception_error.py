#오류 예외처리
# try :
#     ~~~~~~~
# except ZeroDivisionError :
#     ~~~~~~~

'''
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)


#여러개의 오류처리하기.
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

#아래와 같이 한번에 처리도 가능.
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
'''
print("*"*100)
'''
#파일 오픈 에러.
try:
    f = open("나없는파일", 'r')
except FileNotFoundError as e:
    print(e)
print("*"*100)
#오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass
'''
'''
#오류 일부러 발생시키기
# 클래스 상속시키는법. 클래스 생성할때 클래스 이름을 옆에 적어주면 끝
# raise 오류명 
# 

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
'''

'''
#Exception 클래스 상속.
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try :
    say_nick("천사")
    say_nick("바보")
except MyError as e :
    print(e)
'''

