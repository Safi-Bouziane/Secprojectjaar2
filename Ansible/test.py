import os       
import time
import psutil
import requests
import ssl
import ssl
import sys
import certifi

slave1cpu = requests.get('http://192.168.253.149:8000/cpuload', verify = False)
print(slave1cpu.content)
cpu= slave1cpu.content.decode("utf-8") 
print(float(cpu))



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
