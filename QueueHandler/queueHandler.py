#from operator import truediv
#import docker
from testHandler import *
import mysql.connector
from testhttpredirect import *
from geoip import *
from blacklistcheck import *
from sslcheck import *
from dnssec_check import *
from dnsipv6_check import *

#client = docker.client.from_env()

running = []
id: int

#infinite loop over queue
def Queue():
  mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="Honden120",
        database="securityproject"
)
  mycursor = mydb.cursor()
  sql = "SELECT * FROM queue;"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  if len(myresult) != 0:
    mycursor = mydb.cursor()
    item = myresult[0]  
    sql = "DELETE FROM queue LIMIT 1;"
    mycursor.execute(sql)
    mydb.commit()  
    result = ''
    if item[2] and item[1] is not None:
        print('[httptohttpsredirect check]')
        print('---------------------------')
        x = https(item[1])
        print(x)
        result = result + x
    if item[3] and item [0] is not None:
        print('[geoip check]')
        print('---------------------------')
        x = geoip(item [0])
        print(x)
        result =result + x
    if item[4] and item [1] is not None:
        print('[blacklist check]')
        print('---------------------------')
        x = blacklist(item[1])
        print(x)
        result =result + x
    if item[5] and item [1] is not None:
        print('[ssl check]')
        print('---------------------------')
        x = ssl_check(item [1] )
        print(x)
        result =result + x
    if item[6] and item [1] is not None:
        print('[dnssec check]')
        print('---------------------------')
        x = dnscheck(item[1])
        print(x)
        result =result + x
    if item[7] and item [1] is not None:
        print('[ipv6 check]')
        print('---------------------------')
        x = str(ipv6(item[1]))
        print(x)
        result =result + x
    if 1:
        mycursor = mydb.cursor()
        sql = "INSERT INTO `Result`(IP,URL,RESULT,FINISHED) values(%s,%s,%s,%s);"
        val = (item[0], item[1], result, 0)
        mycursor.execute(sql, val)
        mydb.commit()
  else:
   print("database is leeg")
Queue()
