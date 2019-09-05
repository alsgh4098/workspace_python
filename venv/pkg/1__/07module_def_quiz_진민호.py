# #07module_def_quiz.py
# #---------------------------------------
# #총합 계산
# #함수이름: num_sum
# #파라미터: *args
# #결과리턴: 합
# # #---------------------------------------
# def num_sum(*args) :
#     return sum(args)
# print("총합 계산")
# print(num_sum(3,4,6,7,7,8,8,9,9,3,4,23,4,234))
# print()
# print("*"*100)
#
# # # ---------------------------------------
# # 총합 계산
# # 함수이름: num_sum
# # 파라미터: start, end
# # 결과리턴: 합
# # ---------------------------------------
# def num_sum(start, end) :
#     s = start
#     e = end
#     sum = 0
#     for i in range(s, e + 1) :
#         sum += i
#     return sum
#
# # return sum(range(start, end+1)) 도 가능 .
#
# print("총합 계산2")
# print(num_sum(3,6))
# print()
print("*"*100)


#---------------------------------------
#업체정보 등록
#함수이름: add_company
#파라미터: *kwargs  (key는 com_seq,com_name)
#결과리턴: True/False
#---------------------------------------
company_info = list()

def add_company(**kwargs) :
    res = False
    if  type(kwargs) == dict :
        company_info.append(kwargs)
        res = True
        return res
    else :
        return res

add_company( com_seq = 8 , com_name = "kosa")
add_company( com_seq = 2 , com_name = "star")
add_company( com_seq = 4 , com_name = "samsung")
print("업체정보 등록")
# print(company_info)
print("*"*100)

# # #---------------------------------------
# # #업체별 상품정보 등록
# # #함수이름: add_goods
# # #파라미터: com_seq, **kwargs(key는 good_seq,good_name,good_price)
# # #결과리턴: True/False
# # #---------------------------------------
goods_info = list()

def add_goods(com_seq,**kwargs) :
    if type(kwargs) == dict:
        kwargs["com_seq"] = com_seq
        goods_info.append(kwargs)
        res = True
        return res
    else:
        return res

add_goods( 4, good_seq = 23 , good_name = "phone", good_price = "50000000")
add_goods( 4, good_seq = 96 , good_name = "icecream", good_price = "500")
add_goods( 2, good_seq = 77 , good_name = "pencil", good_price = "100")
add_goods( 2, good_seq = 37 , good_name = "wallet", good_price = "1000")
add_goods( 2, good_seq = 65 , good_name = "pen", good_price = "10000")
add_goods( 8, good_seq = 12 , good_name = "cup", good_price = "3000")



# # 등록된 상품리스트 상품데이터 중에서 com_seq를 제외한 또 다른 리스트 만들기
#
# test = {}
# test2 = []
# for i in goods_info :
#         for k,v in i.items() :
#             if k != "com_seq" :
#                 test[k] = v
#         test2.append(test)
#         test = {}
# print("test2",test2)
print("업체별 상품정보 등록")
print("*"*100)

#---------------------------------------
#업체별 상품정보 출력
#함수이름: print_com_goods
#파라미터:   com_seq  (-1=전체출력  / com_seq:해당업체)
#결과리턴: X
#---------------------------------------
def print_com_goods(key) :
    new_key = key
    if type(new_key) != int : # 입력받은 key값이 회사이름일 경우 실행.
        new_com = {} # 입력받은 회사이름과 같은 회사정보(번호,이름)를 넣기 위해서.
        for seq in company_info :
            if seq["com_name"] == key :
                new_com.update(seq)
        new_key = new_com["com_seq"]

    if new_key == -1 : # -1입력 받았을 경우.
        print(goods_info)
    else :
        for g_dic in goods_info : # 위에서 회사이름으로 구한 회사번호 또는 key 값으로 받은
                                  # 회사번호로 상품정보를 출력.
            if g_dic["com_seq"] == new_key :
                print(g_dic)


print("업체번호로 업체별 상품정보 출력")
print("*"*100)

print("업체번호 : 4")
print_com_goods(4)
print()
print("업체번호 : 8")
print_com_goods(8)
print()
print("업체번호 : 2")
print_com_goods(2)
print()
print("업체번호 : -1 -> 전체출력")
print_com_goods(-1)
print()

print("*"*100)
print("업체이름으로 업체별 상품정보 출력")
print("*"*100)

print("업체이름 : samsung")
print_com_goods("samsung")
print()

print("업체이름 : kosa")
print_com_goods("kosa")
print()

print("업체이름 : star")
print_com_goods("star")
print()