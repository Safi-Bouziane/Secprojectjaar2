# GeoIp check

## Bedoeling van de check
Met deze test komen we te weten waar het ip adres gelocaliseerd is.

## Werking van de code
Voor de test hebben we volgende libraries nodig.
```
from geolite2 import geolite2
```

We maken een GeoIp reader aan.
```
reader = geolite2.reader()
```

In volgende sectie code wordt er gecheckt op de locatie van het ip adres en wordt het corresponderende antwoord gereturned.
```
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
```
  