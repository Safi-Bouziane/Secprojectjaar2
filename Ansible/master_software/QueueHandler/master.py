import os
from tqdm import tqdm        
import time
import psutil
import mysql.connector
import requests

def convertTuple(tup):
        # initialize an empty string
    string = ''
    for item in tup:
        string = string  + str(item)+ ","
    string = string[:-1] 
    return string
def startcontainers(row,id):
    sql = f"INSERT INTO result (IP,ID) VALUES (%s,%s);"
    val = (row[0], id)
    mycursor.execute(sql, val)
    mydb.commit()
    if  row[2]:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test1 python3 testhttpredirect.py {row[1]} {id}')
    if  row[3]:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test2 python3 geoip.py {row[0]} {id}')
    if  row[4]:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test3 python3 blacklistcheck.py {row[1]} {id}')
    if  row[5]:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test4 python3 sslcheck.py {row[1]} {id}')
    if  row[6]:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test5 python3 dnssec_check.py {row[1]} {id}')
    if  row[7]:
        os.popen(f'sudo docker run -d argusproof/argusproof_deltateam:test6 python3 dnsipv6_check.py {row[1]} {id}')
def checkdb():
    mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="DeltaGroepPassword#",
        database="securityproject"
)
    mycursor = mydb.cursor()
    mycursor.execute("select count(*) from queue")  
    myresult=mycursor.fetchone()
    if myresult[0] == 0:
        print ("This table is empty!")
        mycursor.close()
        mydb.close()
        time.sleep(3)
        return True
    else:
        mycursor.close()
        mydb.close()
        return False
        
while 1:
    wait = checkdb()
    while wait == False:    
        with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
            mydb = mysql.connector.connect(
            host="securityprojecthowsami.mysql.database.azure.com",
            user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
            password="DeltaGroepPassword#",
            database="securityproject")
            mycursor = mydb.cursor()
            sql = "SELECT * FROM queue;"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if len(myresult) != 0:
                mycursor = mydb.cursor()
                dbbs = myresult[0]
                item = myresult[0]
                sql = "SELECT MAX(ID) FROM result;"
                mycursor.execute(sql)
                id = mycursor.fetchone()
                id = list(id)
                if id[0] == None:
                  id[0] = 0
                cpubar.n = psutil.cpu_percent()
                rambar.n = psutil.virtual_memory().percent
                if cpubar.n < 20 and rambar.n < 20:
                    sql = f"DELETE FROM queue Where id = {dbbs[8]};"
                    mycursor.execute(sql)
                    mydb.commit()
                    startcontainers(item,id[0]+1)
                else:
                    slave1cpu = requests.get('https://192.168.1.10:8000/cpuload', verify = False)
                    slave2cpu = requests.get('https://192.168.1.174:8000/cpuload', verify = False)
                    if slave1cpu > slave2cpu:
                        test = requests.post('https://192.168.1.174:8000/add/', json={"ip": "194.0.6.1","url": "www.ap.be","id": "1","test1": true,"test2": true,"test3": true,"test4": true,"test5": true,"test6": true})
                    else:
                        test = requests.post('https://192.168.1.10:8000/add/', json={"ip": "194.0.6.1","url": "www.ap.be","id": "1","test1": true,"test2": true,"test3": true,"test4": true,"test5": true,"test6": true})
        wait = checkdb()
    