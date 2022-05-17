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
                if id[0] == None:
                  id = 0
                else:
                  id = id[0] + 1
                cpubar.n = psutil.cpu_percent()
                rambar.n = psutil.virtual_memory().percent
                if cpubar.n < 1 and rambar.n < 1:
                    sql = f"DELETE FROM queue Where id = {dbbs[8]};"
                    mycursor.execute(sql)
                    mydb.commit()
                    startcontainers(item,id[0]+1)
                else:
                    slave1cpu = requests.get('http://192.168.253.149:8000/cpuload', verify = False)
                    cpu1= slave1cpu.content.decode("utf-8")
                    cpu1 = float(cpu1)
                    slave2cpu = requests.get('http://192.168.253.150:8000/cpuload', verify = False)
                    cpu2= slave2cpu.content.decode("utf-8") 
                    cpu2 = float(cpu2)
                    if cpu1 < 60 :
                      sql = f"DELETE FROM queue Where id = {dbbs[8]};"
                      mycursor.execute(sql)
                      mydb.commit()
                      print("sent to slave1")
                      print(item)
                      test = requests.post('http://192.168.253.149:8000/add/', json={"ip": item[0],"url": item[1],"id": id,"test1": item[2],"test2": item[3],"test3": item[4],"test4": item[5],"test5": item[6],"test6": item[7]})
                    elif cpu2 < 60:
                      sql = f"DELETE FROM queue Where id = {dbbs[8]};"
                      mycursor.execute(sql)
                      mydb.commit()
                      print(item)
                      print("sent to slave2")
                      test = requests.post('http://192.168.253.150:8000/add/', json={"ip": item[0],"url": item[1],"id": id,"test1": item[2],"test2": item[3],"test3": item[4],"test4": item[5],"test5": item[6],"test6": item[7]})
                    else:
                      print("servers are busy")
                      print(str(cpu1) + "   " + str(cpu2))
                      time.sleep(3)
        wait = checkdb()
