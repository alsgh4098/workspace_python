#module_loop.py

# for 문
# for : 시작점과 끝점이 명확하고, 반복횟수가 명확할 때 사용한다.
# while : 반복문에 특정 조건을 주고싶을 때.
# do while문은 파이썬에 없다.

# 리스트 for문
score_list = ['a','b','c','d']
for score in score_list :
    print(score,"점")

# 포맷코드사용
for score in score_list :
    print("%s 점" %score)

# range for문
# 1에서부터 9까지 2씩 증가시킨 횟수 = range(1,10,2)
for num in range(1,10,2) :
    print(num)
print('*'*100)

for num in range(1,10) :
    print(num)
print('*'*100)
# 파이썬은 ++, --없다.


#range를 활용해서 score_list를 출력하라.
score_list = ['a','b','c','d']
for i in range(len(score_list)) :
    print(score_list[i])
print('*'*100)


# for i in range(4) 끝점 4 전까지, = 1,2,3,4

# for i in range(1,4) 시작점 1부터 끝점 4전까지, = 1,2,3

# for i in range(1,4,2) 시작점 1부터 2씩 증가해서, 끝점 4전까지 = 1,3

#전형적인 for문
test_list = ["one", "two", "three", "four"]

for i in test_list :
    print(i)

#다양한 for문의 사용.
test_list2 = [[1,2],[3,4],[5,6]]

for (i1,i2) in test_list2 :
    print(i1 + i2)

# 구구단
'''
for i1 in range(2,10) :
    print("----------[%d단]----------" %i1)
    for i2 in range(1,10) :
        print("\t   %d x %d = " %(i1,i2) , end = '')
        print( i1 * i2 )
    print("-------------------------")
'''
for i1 in range(2,10) :
    print("----------[%d단]----------" %i1)
    for i2 in range(1,10) :
        print("\t   %d x %d = %d" %(i1 , i2 , i1*i2)) # 위에 구문을 문자열 포멧코드를 활용해서 한줄로
    print("-------------------------")

#가로 출력
for i1 in range(2,10) :
    print("-"*70,"[%d단]"%i1,"-"*70)
    for i2 in range(1,10) :
        print("\t   %d x %d = %d" %(i1 , i2 , i1*i2), end ='')
    print()

#list를 활용해서 출력
dan_list = [2,3,4,5,6,7,8,9]
gob_list = [1,2,3,4,5,6,7,8,9]
for dan in dan_list :
    print("[%d단]" %dan)
    for gob in gob_list :
        print("%d + %d = %d" %(dan,gob,dan*gob), end = '\t')
    print()

#구구단 2,4,6,8단만 찍기.
for i1 in range(2,10,2) :
    print("----------[%d단]----------" % i1)
    for i2 in range(1, 10) :
        print("\t   %d x %d = %d" % (i1, i2, i1 * i2))
    print("-------------------------")

#if문으로 2,4,6,8단만 찍기.
for i1 in range(2,10) :
    if i1%2 == 0 :
        print("----------[%d단]----------" % i1)
        for i2 in range(1, 10) :
            print("\t   %d x %d = %d" % (i1, i2, i1 * i2))
        print("-------------------------")
        

#짝수 구구단 찍기
for i1 in range(2, 10, 2) :
    print("----------[%d단]----------" % i1)
    for i2 in range(2, 10 ,2) :
            print("\t   %d x %d = %d" % (i1, i2, i1 * i2))
    print("-------------------------")

#if문으로 짝수 구구단 찍기
for i1 in range(2,10) :
    if i1%2 == 0 :
        print("----------[%d단]----------" % i1)
        for i2 in range(1, 10) :
            if i2 % 2 == 0 :
                print("\t   %d x %d = %d" % (i1, i2, i1 * i2))
        print("-------------------------")
        
        
# for dictionary
# dictionary에 key값 values값 접근법.

dic = {"uid":"kim","upw":"111","name":"아무개"}
for k in dic :
    print(k)
print("-------------------------")

for v in dic.values() :
    print(v)

print("-------------------------")
print(dic.keys())
print("-------------------------")
print(dic.values())
print("-------------------------")

for k in dic.keys() :
    print( k , ":" , dic[k])

print("-------------------------")
print(dic.items())
print("-----------------------------------------------------------------------------------------------------------")

# while

a = 5
while a > 1 :
    print("big")
    a = a - 1
print("---while done---")

b = 5
while True :
    print("big")
    b = b - 1
    if b < 3 :
        break
print("---while done---")

# while안의 while
# while문으로 구구단찍기

print("while문으로 구구단찍기")
i1 = 2
i2 = 1
while i1 < 10 :
    print("----------[%d단]----------" % i1)
    while i2 < 10 :
        print(" %d x %d = %d" %(i1,i2,i1*i2))
        i2 = i2 + 1
    i2 = 1
    i1 = i1 + 1
    print("-------------------------")

print("-----------------------------------------------------------------------------------------")


# for문안 for문
#*
#**
#***
#****
for i1 in range(1,5,1) :
    for i2 in range(1,i1+1,1) :
        print("*", end = "")
    print("")
print("-----------------------------------------------------------------------------------------")

#****
#***
#**
#*
for i1 in range(5,1,-1) :
    for i2 in range(1,i1,1) :
        print("*", end = "")
    print("")
print("-----------------------------------------------------------------------------------------")
#   *
#  **
# ***
#****
for i1 in range(5,1,-1) :
    for i2 in range(1,i1,1) :
        print(" ", end = "")
    for i2 in range(1, 7-i1, 1) :
        print("*", end = "")
    print("")
print("-----------------------------------------------------------------------------------------")
