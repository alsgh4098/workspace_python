import sqlite3

#db연결

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()


# cursor.execute("select * from polls_question")
# #커서로 안에 항목을 드래그
#
# rows = cursor.fetchall()
# #커서로 드래그한 내용을 전부 가져옴.
#
# for row in rows :
#     print(row)

sql = "select * from polls_question where id=?"
cursor.execute(sql,(2,))
rows = cursor.fetchall()
for row in rows :
    print(row)
# binding : ?값 끼워넣기

sql = "select * from polls_question where id=:val"
cursor.execute(sql,{"val":2})
rows = cursor.fetchall()
for row in rows :
    print(row)
# binding : ?값 끼워넣기

#한개 insert
sql = "insert into polls_question(question_text, pub_date) values(?, datetime('now'))"
cursor.execute(sql, ("이건 2번째 질문", ))
conn.commit()
rows = cursor.fetchall()
for row in rows :
    print(row)

#여러개 insert
data = (("질문1",),("질문2",),("질문3",))
sql = "insert into polls_question(question_text, pub_date) values(?, datetime('now'))"
cursor.executemany(sql, data)
conn.commit()
rows = cursor.fetchall()
for row in rows :
    print(row)

# #삭제 delete
# sql = "delete from polls_question where id = ?"
# cursor.execute(sql, (8, ))
# conn.commit()
rows = cursor.fetchall()
for row in rows :
    print(row)

#
# #변경 set
sql = "update polls_question set question_text=? \
    where id=?"
cursor.execute(sql, ("왓츠뉴스", 2))
conn.commit()
rows = cursor.fetchall()
for row in rows :
    print(row)

# db닫기 conn.close()
# with conn: 으로 안에 전부 넣고 자동닫기도 가능.