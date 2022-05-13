import requests
site = "http://www.hln.be"

responses = requests.get(site)

for response in responses.history:
    print(response.url)
    if "https" in response.url:
        print("https redirectie aanwezig")
        break
