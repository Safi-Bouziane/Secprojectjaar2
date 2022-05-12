import requests
import sys 

responses = requests.get(sys.argv[1])
score = 0

for response in responses.history:
    print(response.url)
    if "https" in response.url:
        print("https redirectie aanwezig")
    else:
        score = 1
if score > 0:
    print("https redirectie niet aanwezig!")


    
