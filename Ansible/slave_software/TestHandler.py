import os
import mysql.connector

def StartTests(ip,id,url,test1,test2,test3,test4,test5,test6):
    mydb = mysql.connector.connect(
    host="securityprojecthowsami.mysql.database.azure.com",
    user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
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
