# Dmarc check

## Bedoeling van de check
In deze test wordt er nagekeken of het domein beschikt over DMARC-records

## werking van de code 
Voor de test hebben we volgende libraries nodig.
```
from dns.resolver
```

We kijken of voor het meegegevern domein er 1 of meerdere TXT records aanwezig zijn. Dit doen we door voor elk TXT record na te gaan of het om een DMARC record gaat.
```
    try:
        result = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
        for record in result:
            if 'DMARC1' in str(result):
                return record
        return "No DMARC record"
    except dns.resolver.NXDOMAIN:
        return "Domain not found"
```
