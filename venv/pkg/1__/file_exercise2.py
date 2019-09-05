import json


# file exercise
f = open("test3",'r', encoding='UTF-8')
line = f.readlines()
print(line)
f.close()

f = open("test3", 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()


with open("json_test", 'r', encoding = 'UTF-8') as f :
    dict_test = json.loads(f.read())
print(dict_test)