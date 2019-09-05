a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}


print(a.items())

print(a.keys())

print(a.values())

print(a)

print('pey' in a) # a는 dict의 키값을 나타냄

print('name' in  a) # value에 접근하기 위해서는 dict에 key값으로 접근해야함.
print('pey' in a.values()) # .values()를 사용하는것도 가능함.

a.clear()
print(a)
