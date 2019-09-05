#03module_f.py
# 오라클에서의 조건문은 아래에 있는 case when then else end
# (case when() then() when() then() else() end)

# 파이썬에서 조건문.
# 괄호 안쓴다.
# 괄호대신에 들여쓰기로 포함관계를 나타낸다.

score = 87
if score >= 90 :
    print("점수는 90점 이상이다.")
print("점수는 90점 이하다.")

print("*"*100)

score = 40
if score >= 90 :
    print("점수는 90이상이다.")
elif score >= 80 :
    print("점수는 80이상이다.")
elif score >= 70 :
    print("점수는 70이상이다.")
elif score >= 60 :
    print("점수는 60이상이다.")
elif score >= 50 :
    print("점수는 50이상이다.")
elif score >= 40 :
    print("점수는 40이상이다.")
elif score >= 30 :
    print("점수는 30이상이다.")
else :
    print("점수는 30미만이다.")

print("*"*100)

# 중첩 if
score = 97
gen = 'm'
if score >= 90 :
    print("90점 이상이다.", end = '')
    if gen == 'm' :
        print(" + 가산점2")
    else :
        print("가산점0")
elif score >= 80 :
    print("80점 이상이다.", end='')
    if gen == 'm' :
        print("가산점2")
    else :
        print("가산점0")
elif score >= 70 :
    print("70점 이상이다.", end='')
    if gen == 'm' :
        print("가산점2")
    else :
        print("가산점0")
elif score >= 60 :
    print("60점 이상이다.", end='')
    if gen == 'm' :
        print("가산점2")
    else :
        print("가산점0")
else :
    print("점수미달")
