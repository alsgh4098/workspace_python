# 위치인자 언패킹


# def abc(a,b,c) :
#     return b, a, c
# p = [ 5, 7, 9]
#
# print(abc(*p))
# print()


# print(abc(p))
# 에러. 함수 abc()는 인자로 세개의 값을 받기 때문에
# abc(p)로 함수호출을 끝낼경우에, abc함수에서 필요한 세가지 인자가 없기 때문에,
# 여기서 헷갈릴수 있는점은 p는 리스트로 안에 5, 7, 9 세개의 값이 있기 때문에
# abc(p)를 abc(5,7,9)와 같은 의미라고 생각할 수 있지만
# abc(p)는 abc([5,7,9])이고 이 경우엔 [5,7,9] 리스트 하나를 a에 받기때문에
# 필요한 인자 b, c가 없게된다.
# 따라서 언패킹을 통해 리스트를 풀어줘야한다.
# *[5,7,9]는 5,7,9와 같은의미.

# 키워드인자 언패킹
goods_sequence = 0
goods_list = []

def add_goods(com_seq, **kwargs) :
    global goods_sequence
    goods_sequence = goods_sequence + 1
    kwargs["com_seq"] = com_seq
    kwargs["goods_seq"] = goods_sequence
    goods_list.append(kwargs)
    return True

# add_goods(1, com_seq = 1, good_name = "상품명 1", good_price = "5000")

add_goods(com_seq = 1, good_name = "상품명 1", good_price = "5000")

add_goods(1, good_name = "상품명 1", good_price = "5000")

print(goods_list)