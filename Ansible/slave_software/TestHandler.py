import os
import mysql.connector

def StartTests(ip,id,url,test1,test2,test3,test4,test5,test6,test7,test8):
    mydb = mysql.connector.connect(
    host="secproject.mysql.database.azure.com",
    user="argususer",
    password="DeltaGroepPassword#",
    database="securityproject")
    mycursor = mydb.cursor()
    sql = f"INSERT INTO result (IP,ID) VALUES (%s,%s);"
    val = (ip, id)
    mycursor.execute(sql, val)
    mydb.commit()
    if  test1:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test1 python3 testhttpredirect.py {url} {id}')
    if  test2:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test2 python3 geoip.py {ip} {id}')
    if  test3:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test3 python3 blacklistcheck.py {url} {id}')
    if  test4:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test4 python3 sslcheck.py {url} {id}')
    if  test5:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test5 python3 dnssec_check.py {url} {id}')
    if  test6:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test6 python3 dnsipv6_check.py {url} {id}')
    if  test7:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test7 python3 dmarc.py {url} {id}')
    if  test8:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test8 python3 spf.py {url} {id}')




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
