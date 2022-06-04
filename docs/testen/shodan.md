# Shodan check

## Bedoeling van de check
Bij deze check wordt er via shodan allerlei informatie binnengehaald over het meegegeven ip adres.

## Werking van de code
Voor de test hebben we volgende libraries nodig.
```
import os
```

In onderstaande code vragen we de informatie op van het ip adres.
```
def shodan():
    ip = sys.argv[1]
    x = os.system(f'curl -X GET "https://api.shodan.io/shodan/host/{ip}?key=b2kVKUUFHe0bjBcrB1mhr1S8YLz0myx8"')
```

Deze check hebben we niet geïmplementeerd in de resultaten van de database. Dit wegens de zeer grote, en onoverzichtelijke, informatie die we terug krijgen.