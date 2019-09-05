# 함수이름 : add_hp
# 파라미터 : ( key : name , tel ) xxxx **kwargs
# 결과리턴 : True / False

'''
hp_list = []

def add_hp(**user_info) :
    print(user_info)
    # appen로 딕셔너리를 리스트에 추가하면 리스트안에 딕셔너리로 들어간다.
    hp_list.append(user_info)
    # 딕셔너리를 리스트에 extend하면 딕셔너리 키값이 리스트 값으로 들어간다.
    #hp_list.extend(user_info)
    return True

res = add_hp(name = "홍길동" , tel = "111")

if res :
    print("저장되었습니다.")
else :
    print("다시 저장해주세요.")

print(hp_list)
'''

'''
def maxmin(*number_list):
    max_num = max(number_list)
    min_num = min(number_list)
    return max_num, min_num

(rexmax, rexmin) = maxmin(*[3, 4, 99], *[9, 3], *[6, 1, 4, 8])
print(rexmax, rexmin)
'''
'''
[[3, 4, 99], [9, 3], [6, 1, 4, 8]]

# 리스트 안의 리스트 최대 최솟값 구하기.
def maxmin(*number_list):
    max_list_num = []
    min_list_num = []
    for num in number_list :
        max_list_num.append(max(num))
        min_list_num.append(min(num))
    max_num = max(max_list_num)
    min_num = min(min_list_num)
    return max_num, min_num

(rexmax, rexmin) = maxmin([3, 4, 99], [9, 3], [6, 1, 4, 8])
print(rexmax, rexmin)

# for문 2개 그리고 max, min함수 안쓰고 리스트 안의 리스트 최대 최솟값 구하기.
def maxmin(*number_list) :
    max_num = -100000
    min_num = 100000
    for list in number_list :
        for num in list :
            if max_num < num :
                max_num = num
            elif num < min_num :
                min_num = num
    return max_num, min_num
(rexmax, rexmin) = maxmin([3, 4, 99], [9, 3], [6, 1, 4, 8])
print(rexmax, rexmin)
'''

# # ---------------------------------
# # 전화번호 목록 ( list_hp 출력 )   |
# # 함수이름 : print_hp              |
# # 파라미터 : x                     |
# # 결과리턴 : x                     |
# # ---------------------------------
#
# info_p = [{"name" : "진민호", "Pnum" : "010-3430-4098"}]
#
# def print_hp(list_hp) :
#     for info in list_hp :
#             print(info.values())
# info_p.append({"name" : "효준", "Pnum" : "010-2345-4564"})
# print_hp(info_p)
#
# print("*"*100)
# def print_hp(list_hp) :
#     for info in list_hp :
#         for val in info.values() :
#             print(val, end= '')
#             print(" ", end= '')
#         print()
#
# print_hp(info_p)
#
#
# print("*"*100)
# def print_hp(*list_hp) :
#     for info in list_hp :
#         for val in info :
#             print(val.values())
#
# print_hp(info_p)

#
# print("*"*100)
# def print_hp(**list_hp) :
#     print(list_hp)
#     print(type(list_hp))
#     for val in list_hp.values() :
#         print(val)
# print_hp( name = "진민호", Pnum = "010-3430-4098" )
#

# ---------------------------------
# 전화번호 수정 ( list_hp 출력 )   |
# 함수이름 : update_hp             |
# 파라미터 : seq, key, value       |
# 결과리턴 : T or F                |
# ---------------------------------
# 원하는 key값을 선택해서 그 안의 value값을 변경해주는 함수.

# list_info = [{"name":"jin","pnum":"01030405060","seq":1},
#             {"name":"kin","pnum":"0175675674","seq":2},
#             {"name":"lee","pnum":"01134534535","seq":3}]
#
# def update_hp(seq, key,value) :
#         res = False
#         if 0 < seq < len(list_info):
#             list_info[seq-1][key] = value
#             res = True
#             return res
#         else :
#             print("seq error")
#             res = False
#             return res
#
# print(list_info)
#
# print("*" * 100)
# update_hp(2,"name","woo")
# print(list_info)
#
# print("*" * 100)
# update_hp(1,"pnum","0132156231564")
# print(list_info)

'''
list_info = [{"name":"jin","pnum":"01030405060","seq":1},
            {"name":"kin","pnum":"0175675674","seq":2},
            {"name":"lee","pnum":"01134534535","seq":3}]
# \딕셔너리로 받아서 키값에 따른 데이터 찾는법.

def update_hp(seq, **kwargs) :
        res = False
        k_key = ""
       # 여기 함수 안에서 kwargs의 key값을 모른다고 가정할 때 key값을 알고싶고, 사용하고싶으면 어떻게 하는지.
       # 나는 for문으로 딕셔너리에 접근하면 사용할 인자가 key값을 갖는걸 이용했는데,
       # 다른 방법이 있는지, keys()함수는 key리스트를 불러와서 안됨.
       # print(kwargs.)
        print(kwargs)
        
        if 0 < seq < len(list_info) :
            for key in kwargs:
                k_key = key
                print(key)
            list_info[seq-1][k_key] = kwargs[k_key]

            res = True
            return res
        else :
            print("seq error")
            res = False
            return res


print("*" * 100)
update_hp(2,name = "jan")
print(list_info)


print("*" * 100)
update_hp(1,pnum = "123124123")
print(list_info )
'''

list_info = [{"name": "jin", "pnum": "01030405060", "seq": 1},
             {"name": "kin", "pnum": "0175675674", "seq": 2},
             {"name": "lee", "pnum": "01134534535", "seq": 3}]


# \딕셔너리로 받아서 키값에 따른 데이터 찾는법.

def update_hp(seq, **kwargs):
    res = False
    k_key = ""
    print(kwargs.keys())

    if 0 < seq < len(list_info):
        for k in kwargs.keys():
            print(k)
            list_info[seq - 1][k] = kwargs[k]

        res = True
        return res
    else:
        print("seq error")
        res = False
        return res


print("*" * 100)
update_hp(2, name="jan")
print(list_info)

'''
list_info = [{"name": "jin", "pnum": "01030405060", "seq": 1},
             {"name": "kin", "pnum": "0175675674", "seq": 2},
             {"name": "lee", "pnum": "01134534535", "seq": 3}]


# \딕셔너리로 받아서 키값에 따른 데이터 찾는법.

def update_hp(seq, **kwargs):
    res = False
    k_key = ""
    print(kwargs)

    if 0 < seq < len(list_info):
        for k ,v  in kwargs.items():
            print(k , v)
            list_info[seq - 1][k] = v

        res = True
        return res
    else:
        print("seq error")
        res = False
        return res


print("*" * 100)
update_hp(2, name="jan")
print(list_info)

'''