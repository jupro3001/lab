import mysql.connector as mysq
from datetime import datetime
con = mysq.connect(host="localhost",user="root",password="Password@123")
cur = con.cursor()
if con.is_connected():
    print("success")
else:
    exit()
        
q="create database CSproject;"
cur.execute(q)
print("Database created successfully")
q="use CSproject;"
cur.execute(q)
