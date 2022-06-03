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
