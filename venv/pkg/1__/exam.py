
addr = []


addr  = ["서울시","군포시","안양시"]


for 도시이름 in addr :
     print(도시이름)

u_dict = { "uname" : "jinminho" , "uid" : "jmh"}
for i in u_dict :
    print(i)

print(u_dict.keys())
print(u_dict.values())

u_dict["addr"] = "서울시"

Item_list = [['a1','a2','a3'], 'b', 'c', {'d' : 'D'}]
print(Item_list)



#틀린것
# dictionary에 접근하는 방법
# 키값따로, 벨류값 따로.
# 리스트 추가 list = [] 에서 list[0] = ? 안됨.

#Key 리스트 만들기(keys)

a = {'name':'pey','phone':'01034304098','birht':'1118'}
for str in a.keys() :
    print(str)
print("*"*100)
for str in a.values() :
    print(str)
print("*"*100)
for str in a :
    print(str)
print("*" * 100)