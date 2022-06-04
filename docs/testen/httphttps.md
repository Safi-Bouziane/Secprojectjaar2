# HTTP to HTTPS redirectie

## Bedoeling van de check
Met deze test komen we te weten waar het ip adres gelocaliseerd is.

## Werking van de code
Voor de test hebben we volgende libraries nodig.
```
import requests
```

We kijken of de ingegeven url geldig is.
```
try:
     website = requests.get(Url)
    except:
        return "check failed"
```

Nadien checken we of er https redirectie aanwezig is.
```
url = website.url
if url.startswith(('https://')):
    return "https redirectie aanwezig."
else:
    return"https niet redirectie aanwezig!!!"
```