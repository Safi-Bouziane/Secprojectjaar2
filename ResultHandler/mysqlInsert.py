
import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="myuser",
 password="mypass",
 database="SecurityProject"
)
def InsertIntoBackup(IP,TEST1,TEST2,RESULT):
    mycursor = mydb.cursor()
    sql = "INSERT INTO `Backup`(IP,TEST1,TEST2,result) values(%s,%s,%s,%s);"
    val = (IP, TEST1, TEST2,RESULT)
    mycursor.execute(sql, val)

    mydb.commit()
