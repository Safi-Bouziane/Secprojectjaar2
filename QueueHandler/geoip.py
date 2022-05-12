#https://stackoverflow.com/questions/32575666/python-geoip-does-not-work-on-python3-4
#deel code is van grepper (het verkijgen van de ip)
from geolite2 import geolite2
import socket #module for gethostbyname
import sys 
def geoip(Ip):
  ip = Ip
  reader = geolite2.reader()


  match = reader.get(ip)
  if match:
    # print(match)
    if 'country' in match:
     return(match['country']['iso_code'])
    else:
     return (match['continent']['code'])
  else:
     return('')