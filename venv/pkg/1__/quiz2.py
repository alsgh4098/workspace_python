#07module_def_quiz.py
#---------------------------------------
#총합 계산
#함수이름: num_sum
#파라미터: *args
#결과리턴: 합
# #---------------------------------------
def num_sum(*args) :
    return sum(args)
print("총합 계산")
print(num_sum(3,4,5,6))
print()
print("*"*100)

# # ---------------------------------------
# 총합 계산
# 함수이름: num_sum
# 파라미터: start, end
# 결과리턴: 합
# ---------------------------------------
def num_sum(start, end) :
    s = start
    e = end
    sum = 0
    for i in range(s, e + 1) :
        sum += i
    return sum

print("총합 계산2")
print(num_sum(3,6))
print()
print("*"*100)
# #---------------------------------------
# #업체정보 등록
# #함수이름: add_company
# #파라미터: *kwargs  (key는 com_seq,com_name)
# #결과리턴: True/False
# #---------------------------------------
company_info = list()

def add_company(**kwargs) :
    res = False
    if  type(kwargs) == dict :
        company_info.append(kwargs)
        res = True
        return res
    else :
        return res

add_company( com_seq = 4 , com_name = "kosa")
add_company( com_seq = 2 , com_name = "kosta")
add_company( com_seq = 8 , com_name = "samsung")
print("업체정보 등록")
print(company_info)
print()
print("*"*100)

# #---------------------------------------
# #업체별 상품정보 등록
# #함수이름: add_goods
# #파라미터: com_seq, **kwargs(key는 good_seq,good_name,good_price)
# #결과리턴: True/False
# #---------------------------------------
goods_info = list()

def add_goods(com_seq,**kwargs) :
    if type(kwargs) == dict:
        kwargs["com_seq"] = com_seq
        goods_info.append(kwargs)
        res = True
        return res
    else:
        return res


add_goods( 1, good_seq = 96 , good_name = "icecream", good_price = "500")
add_goods( 2, good_seq = 77 , good_name = "pencil", good_price = "1000")
add_goods( 3, good_seq = 1233 , good_name = "cup", good_price = "3000")

print("업체별 상품정보 등록")
print(goods_info)
print()
print("*"*100)

#---------------------------------------
#업체별 상품정보 출력
#함수이름: print_com_goods
#파라미터:   com_seq  (-1=전체출력  / com_seq:해당업체)
#결과리턴: X
#---------------------------------------
def print_com_goods(com_seq) :
    if com_seq == -1 :
        print(goods_info)
    else :
        for g_dic in goods_info :
            if g_dic["com_seq"] == com_seq :
                print(g_dic)

print("업체별 상품정보 출력")
print("업체번호 : 3")
print_com_goods(3)
print("업체번호 : 1")
print_com_goods(1)
print("업체번호 : -1 -> 전체출력")
print_com_goods(-1)
print("*"*100)