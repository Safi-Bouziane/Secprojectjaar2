import requests

x = requests.get('https://10.211.55.12:8000/cpuload', verify = False)
print(x.text)