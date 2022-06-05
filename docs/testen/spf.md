# SPF record check

## Bedoeling van de check
In deze test wordt er nagekeken of het domein beschikt over SPF-records

## werking van de code 
Voor de test hebben we volgende libraries nodig.
```
from dns.resolver
```

We kijken of voor het meegegevern domein er 1 of meerdere TXT records aanwezig zijn. Dit doen we door voor elk TXT record na te gaan of het om een spf record gaat.
```
try:
        result = dns.resolver.resolve(domain, 'TXT')
        for record in result:
            if 'spf1' in str(record):
                return record
        return "No SPF record"
    except dns.resolver.NXDOMAIN:
        return "Domain not found"
```