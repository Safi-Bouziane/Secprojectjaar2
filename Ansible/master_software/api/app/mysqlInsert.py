
import mysql.connector
def make_db_conn(mydb):
    mydb = mysql.connector.connect(
    host="securityprojecthowsami.mysql.database.azure.com",
    user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
    password="Honden120",
    database="securityproject"
    )
    return mydb
def InsertIntoQueue(IP, RESULT, TEST1, TEST2, TEST3, TEST4, TEST5, TEST6, TEST7, TEST8):
    mydb = make_db_conn(mydb)
    mycursor = mydb.cursor()
    sql = "INSERT INTO `queue`(IP,URL,TEST1,TEST2,TEST3,TEST4,TEST5,TEST6, TEST7, TEST8) values(%s,%s,%s,%s,%s,%s,%s,%s);"
    val = (IP, RESULT, TEST1, TEST2, TEST3, TEST4, TEST5, TEST6, TEST7, TEST8)
    mycursor.execute(sql, val)

    mydb.commit()

#/***************************************************************
#*
#* Copyright (Wouter Weemaes, Safi Bouziane, Kamil Grielens, Robbe Willeme) - All rights reserved. 
#*
#* Unauthorized use, copy, modify, merge, publish, distribute, sublicense, 
#* and/or sell any parts of the software/source code is strictly prohibited.
#* Proprietary and confidential
#* License: No license. 
#* Written by: (Wouter Weemaes) (wouterweemaes@outlook.com), (06/2022)
#*
#****************************************************************/
