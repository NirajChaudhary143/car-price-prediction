import sqlite3

# sqlite creation and connection

conn = sqlite3.connect("car_price.db")
cursor = conn.cursor()

sql="""
CREATE TABLE car_detail (
    name TEXT,
    company TEXT
) """

cursor.execute(sql)
print("Database created")
conn.commit()
conn.close()