import requests
import sys
def https(Url):
    website = requests.get(Url)
    url = website.url
    score = 1
    finished = 0

    if url.startswith(('https://')):
        return "https redirectie aanwezig."
    else:
        return"https niet redirectie aanwezig!!!"

