#https://stackoverflow.com/questions/32575666/python-geoip-does-not-work-on-python3-4
#deel code is van grepper (het verkijgen van de ip)
from geolite2 import geolite2
import socket #module for gethostbyname
import sys 

website = sys.argv[1]# you can put any website
ip = socket.gethostbyname(website)
reader = geolite2.reader()


match = reader.get(ip)
if match:
  # print(match)
  if 'country' in match:
    print(match['country']['iso_code'])
  else:
    print(match['continent']['code'])
else:
  print('')