#from operator import truediv
#import docker
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
def Queue(item):
  item = item.split(',')
  result = ''
  if item[2] and item[1] is not None:
        print('[httptohttpsredirect check]')
        print('---------------------------')
        try:
          x = https(item[1])
        except:
          x = "httpredirectcheck failed"
        result = result + x
  if item[3] and item [0] is not None:
        print('[geoip check]')
        print('---------------------------')
        try: 
          x = geoip(item [0])
        except:
          x = "geoipcheck failed"
        print(x)
        result =result + x
  if item[4] and item [1] is not None:
        print('[blacklist check]')
        print('---------------------------')
        try:
          x = blacklist(item[1])
        except:
          x = "blacklistcheck failed"
        result =result + x
  if item[5] and item [1] is not None:
        print('[ssl check]')
        print('---------------------------')
        try:
          x = ssl_check(item [1])
        except:
           x = "sslcheck failed"
        result =result + x
  if item[6] and item [1] is not None:
        print('[dnssec check]')
        print('---------------------------')
        try: 
          x = dnscheck(item[1])
        except:
           x = "dnscheck failed"
        result =result + x
  if item[7] and item [1] is not None:
        print('[ipv6 check]')
        print('---------------------------')
        try:
          x = str(ipv6(item[1]))
        except:
           x = "ipv6check failed"
        result =result + x
  if 1:
        mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="DeltaGroepPassword#",
        database="securityproject")
        mycursor = mydb.cursor()
        sql = "INSERT INTO `Result`(IP,URL,RESULT,FINISHED) values(%s,%s,%s,%s);"
        val = (item[0], item[1], result, 0)
        mycursor.execute(sql, val)
        mydb.commit()
Queue(sys.argv[1])


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
