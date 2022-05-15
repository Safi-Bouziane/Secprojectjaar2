#https://stackoverflow.com/questions/32575666/python-geoip-does-not-work-on-python3-4
#deel code is van grepper (het verkijgen van de ip)
import mysql.connector
from geolite2 import geolite2
import socket #module for gethostbyname
import sys 
def geoip(Ip):
  ip = Ip
  reader = geolite2.reader()

  try:
   match = reader.get(ip)
  except:
    return "check failed"
  if match:
    # print(match)
    if 'country' in match:
     return(match['country']['iso_code'])
    else:
     return (match['continent']['code'])
  else:
     return('No match')
result = geoip(sys.argv[1])
rowid = sys.argv[2]
if 1:
        mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="DeltaGroepPassword#",
        database="securityproject")
        mycursor = mydb.cursor()
        sql = f"UPDATE Result SET TEST2 = %s WHERE ID = %s"
        val = (result,rowid)
        mycursor.execute(sql, val)
        mydb.commit()