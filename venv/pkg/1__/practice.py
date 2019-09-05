print("hello world")
print('--'*50)
print("Mary\'s cosmetics")
print('--'*50)
print("신씨가 소리질렀다. \"도둑이야\".")
print('--'*50)
print("\"C:\\Windows")
print('--'*50)
print("안녕하세요.\n만나서\t\t반갑습니다.")
print('--'*50)
print ("오늘은", "일요일")
print('--'*50)
print("naver/kakao/sk/samsung")
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print("first",end = '')
print("second")
string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(string))

s = "hello"
t = "python"
print(s+t)
print("Hi" * 3)

print('*'*80)


t1 = 'python'
t2 = 'java'

print((t1+' '+t2+' ')*3)

print(2 + 2 * 3 ) # 8

a = '132'
print(type(a)) # str

num_str = "720"

num = 100

print(int(num_str))
print(str(num))

print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)

lang = 'python'

print(lang[0],lang[2])

license_plate = "24가 2210"

print(license_plate[4:8])

string = "홀짝홀짝홀짝"
print(string[0]+string[2]+string[4])

string = "PYTHON"
print(string[5]+string[4]+string[3]+string[2]+string[1]+string[0])

phone_number = "010-1111-2222"
print(phone_number[0:3],phone_number[4:8],phone_number[9:13])

print(phone_number[0:3]+phone_number[4:8]+phone_number[9:13])

url = "http://sharebook.kr"
print(url[17:19])





print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)

# aBcd가 아닙니다. abcd 가 출력됩니다.
# 주의하세요. replace 메서드는 기존의 문자열을 변경하는 것이 아니라
# 변경된 문자열을 새롭게 생성해줍니다. 따라서 replace
# 메서드가 전달해주는 값을 변수에 바인딩 후 사용해야 합니다.
# 아래 코드에서 new_string에는 aBcd 값이 저장됩니다.
string1 = 'abcd'
string1.replace('ab', 'AB')
print(string1)
#아래껀 됨.
string1 = 'abcd'
string2 = string1.replace('ab', 'A')
print(string2)

#028
#아래 코드의 실행 결과를 예상하라
#lang = 'python'
#lang[0] = 'P'
#print(lang)

#'Python'을 예상했겠지만 에러가 발생합니다. 기존에 생성한 문자열은 변경 할 수 없습니다.
#TypeError: 'str' object does not support item assignment
#Python을 바인딩하고 싶다면, 아래와 같이 새롭게 문자열을 생성하고 lang이 생성한 문자열을 가리키게 해야합니다.
#lang = 'Python'

print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)
print('--'*50)

movie_rank = ["닥터 스트레인지","스플릿","럭키"]
print(movie_rank)

movie_rank.append("배트맨")
print(movie_rank)


movie_rank.remove("배트맨")
print(movie_rank)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = []
langs.extend(lang1)
langs.extend(lang2)
print(langs)

nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))
print(sum(nums))

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

nums = [1, 2, 3, 4, 5]
#print(avg(nums))
#평균함수 없음
print(sum(nums)/len(nums))