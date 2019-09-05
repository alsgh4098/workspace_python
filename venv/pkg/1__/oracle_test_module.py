import cx_Oracle
dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
# dsn =  database source name, data source name
db = cx_Oracle.connect("kosa", "0000", dsn)
cursor = db.cursor()
cursor.execute("""SELECT * FROM emp""")
row = cursor.fetchone()
print(row)