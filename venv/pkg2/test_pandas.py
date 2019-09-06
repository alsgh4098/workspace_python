import pandas as pd
import os
import sqlite3

def common_dbconn():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = BASE_DIR + "\db.sqlite3"
    conn = sqlite3.connect(db_path)
    return conn


mon = [3,7,9]

data = {"kor":[100,90,80] , "math":[44,33,55] }

df = pd.DataFrame(data, index = mon)

print(df)

conn = common_dbconn()
df.to_sql("pandas_score", conn, if_exists="replace" )


#dataframe화 됐음.
rows = pd.read_sql("select * from pandas_score", conn)

print(rows)


# with conn:
#     sql = ("insert into board_sql(title,content,reg_id,reg_date) values(?,?,?, datetime('now'))")
#     cursor = conn.cursor()
#     cursor.execute(sql, (val_title, val_content, val_regid))
#     conn.commit()

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["axes.grid"] = True
df.plot()
plt.show()

df = pd.read_csv("C:/kosa/workspace_python/venv/pkg2/sales_data.csv")
monthList  = df ['month_number'].tolist()
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
shampooSalesData   = df ['shampoo'].tolist()
moisturizerSalesData = df ['moisturizer'].tolist()
plt.plot([],[],color='m', label='face Cream', linewidth=5)
plt.plot([],[],color='c', label='Face wash', linewidth=5)
plt.plot([],[],color='r', label='Tooth paste', linewidth=5)
plt.plot([],[],color='k', label='Bathing soap', linewidth=5)
plt.plot([],[],color='g', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)
plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData,
              bathingsoapSalesData, shampooSalesData, moisturizerSalesData,
              colors=['m','c','r','k','g','y'])
plt.xlabel('Month Number')
plt.ylabel('Sales unints in Number')
plt.title('Alll product sales data using stack plot')
plt.legend(loc='upper left')
