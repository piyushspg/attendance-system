#!C:\Users\piyush\miniconda3\python.exe
import mysql.connector


print("Content-Type: text/html\n")
conn = mysql.connector.connect(host="localhost", user="root", database="sms")
cursor=conn.cursor()

selectquery="select * from students"
cursor.execute(selectquery)
records=cursor.fetchall()
print("no. of students in the university",cursor.rowcount)

for row in records:
    print("student no",row[0])
    print("roll number", row[1])
    print("name", row[2])
    print("father_name", row[3])
    print("class", row[4])
    print("mobile", row[5])
    print("email", row[6])

cursor.close()
conn.close()
