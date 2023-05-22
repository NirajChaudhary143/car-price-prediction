import sqlite3

connection = sqlite3.connect("car_price.db")
cur = connection.cursor()

with open('./Name_Company.csv','r') as file:
    records= 0
    for row in file:
        cur.execute('insert into car_detail values (?,?)', row.split(","))
        connection.commit()
        records += 1
connection.close()
print("\n{} Records Tranfer COmplete".format(records))
