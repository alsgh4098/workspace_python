import json
with open( 'test.txt', 'r', encoding='UTF-8' ) as f :
    dic_data = json.loads(f.read())
    for i in range(0, len(dic_data["data"])) :
        print(  dic_data["data"][i]["user"]  )

