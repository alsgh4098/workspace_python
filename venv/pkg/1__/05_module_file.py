# 05module_file
import os
'''
f1 = open("test", "r")

line = f1.readline()

print(line)



print(line)

f2 = open("test", "a")
f2.write("\nzzz11")
f2.close()

with open("test", "a") as f:
    f.write("\nzzzzz77")
    f.write("\nzzzzz88")

# 파일생성.
f3 = open("C:/kosa/workspace_python/venv/pkg/test2", "w")
f3.close()

# 기존파일열기
'''

#파일을 읽어서 user정보만 출력하기.
import json
with open( 'test.txt', 'r', encoding='UTF-8' ) as f :
        # loads = 제이슨타입(키,벨류)을 스트링으로 디코딩
        # dumps = 제이슨타입(키,벨류) 스트링으로 디코딩
    print(   json.loads(f.read()) ["data"][0]["user"]["username"]   )

    #str_data = f.read()
    #dict_data = json.loads(f.read())
    #print(dict_data["data"][0]["user"]["username"])

    # for line in f.readlines() :
    #     line = line.strip() # .strip : 문장의 앞 뒤, 공백제거
    #     line = line.replace("\n","") # 줄바꿈 제거.

    #     if line == "\"user\": {":
    #         print(test.txt["data"][0]["user"]["username"])

    # meta 가져오기
    import json

    with open('test.txt', 'r', encoding='UTF-8') as f:
        print(json.loads(f.read())["meta"])
'''
os.listdir("C:/kosa/workspace_python/venv/pkg")
'''
print("*" * 100)
# #현재 디렉토리 출력하기.
# print(os.getcwd())

test_dict =  {"location": "null",\
              "filter": "Normal",\
              "created_time": "1440501087"}

print(test_dict)
print(type(test_dict))

#json.dumps

test_str = json.dumps(test_dict)
print(test_str)
print(type(test_str))

#출력값의 따옴표차이. '와 "
#json패키지는 반드시 양따옴표로 묶여있어야함.
#json.dumps는 dict타입을 string으로
#json.loads는 string타입을 dict타입으로
#파일을 읽어서 안에 있는 내용을 dict타입으로 받아 정리하기위해서는 json.loads를 사용한다.
