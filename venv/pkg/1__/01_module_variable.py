#module_variable.py

a = 3
b = 2

print(a+b)

a = "hello"


print(a)

print(a*2) # hellohello

#print(a-2) # error

print('A')
print('B')
print('C')
#파이썬에는 \n print마지막에 항상 숨어들어있다
#아래처럼 end를 없애주면 \n이 사라진다.
print()
print('A', end='')
print('B', end='')
print('C', end='')

print('\n''a''b''c')

print()

print('A', end='\t')
print('B', end='\t')
print('C', end='\n')

print()

# ,는 사이 공백이 생김
# 붙여쓰기와 +는 생기지 않음.

# 여기서 변수 a는 hello 문자열을 담고있다.

print(a,"EFG","H")

print(a+"EFG"+"H")

print(a,"EFG""H")
print("------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------")
age = 28
name = "아무개"

print("아무개는",age,"살입니다.")

#print("아무개는"+age+"살입니다.") # 에러, 문자열과 숫자형 변수를 '+'로 합칠수 없음.

#포멧형출력이 가장 편함.
print("%s는 %d살 입니다." %(name,age))

# input함수는 항상 문자열로 값을 받는다.
'''
age = input("나이는 ?")

print("%s살 이시군요." %(age))

# 문자열로 받은 값을 숫자형으로 변환하기를 원한다면
# int()로 캐스팅
print("삼년후에는 %d살 이시군요."%(int(age)+3))

#list[] tuple() dic{}

#list = 배열 : 변수하나에 여러 값을 담기위한 변수.
'''
print("------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------")
list = [1,2,'a',"ABC",[1,['a','b','c']]]

print(len(list))

print(list[4])

print(len(list[4]))

print(list[4][1][1])


list2 = [1,2,3]
list2.append(4)
print(list2)

list2[3] = 'aa'
print(list2)
list2.remove('aa')
print(list2)
del list2[0]
print(list2)
print("------------------------------------------------------------------------------------------")
#tuple : list의 상수형이다.(고정불변) read only
tuple = (1,2,3)
print(tuple[0])
print(tuple[1])
print(tuple[2])
# tuple[1] = 3 //error 튜플 수정불가.
print("------------------------------------------------------------------------------------------")
#dictionery (key : value) <- 제이슨 표기법(key : value) java script object notaion


dic = { "uid":"kim" ,  "upw":"111" , "gen":"f" }

print(dic)

print(dic["uid"])

dic["addr"] = "seoul" # key값,value 새로 생성.
print("------------------------------------------------------------------------------------------")
print(dic)

dic["addr"] = "busan"
print(dic)

del dic["addr"] # addr키값 삭제
print(dic)

video = {
 "kind": "youtube#videoListResponse",
 "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/sDAlsG9NGKfr6v5AlPZKSEZdtqA\"",
 "videos": [
  {
   "id": "7lCDEYXw3mM",
   "kind": "youtube#video",
   "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/iYynQR8AtacsFUwWmrVaw4Smb_Q\"",
   "snippet": {
    "publishedAt": "2012-06-20T22:45:24.000Z",
    "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "title": "Google I/O 101: Q&A On Using Google APIs",
    "description": "Antonio Fuentes speaks to us and takes questions on working with Google APIs and OAuth 2.0.",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/default.jpg"
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/mqdefault.jpg"
     },
     "high": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/hqdefault.jpg"
     }
    },
    "categoryId": "28"
   },
   "contentDetails": {
    "duration": "PT15M51S",
    "aspectRatio": "RATIO_16_9"
   },
   "statistics": {
    "viewCount": "3057",
    "likeCount": "25",
    "dislikeCount": "0",
    "favoriteCount": "17",
    "commentCount": "12"
   },
   "status": {
    "uploadStatus": "STATUS_PROCESSED",
    "privacyStatus": "PRIVACY_PUBLIC"
   }
  }
 ]
}
print("------------------------------------------------------------------------------------------")
#비디오의 아이디, 제목,  썸네일의 default url
print("id  : ",video["videos"][0]["id"])

print("title  : ", video["videos"][0]["snippet"]["title"])

print("url  : ", video["videos"][0]["snippet"]["thumbnails"]["default"]["url"])

print("------------------------------------------------------------------------------------------")

list3 = [1,2,'a',"ABC",[1,{'a':1 ,'b':[0,{'k':1,'k2':2}] ,'c':3}]]

print(list3[4][1]["b"])
print("------------------------------------------------------------------------------------------")
print(" id  : ",video["videos"][0]["id"],'\n',"title  : ",video["videos"][0]["snippet"]["title"],'\n',"url  : ",video["videos"][0]["snippet"]["thumbnails"]["default"]["url"])
print("------------------------------------------------------------------------------------------")


