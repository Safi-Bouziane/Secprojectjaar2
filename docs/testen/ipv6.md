# DNS Ipv6 check

## Bedoeling van de check
Deze test kijkt na of er AAAA DNS records aanwezig zijn voor het domein.

## Werking van de code
Voor de test hebben we volgende libraries nodig.
```
import dns.resolver
```

We kijken na of er voor het meegegeven domein AAAA records aanwezig zijn. En geven het correcte resultaat terug.
```
try:
        result = my_resolver.resolve(domain, "AAAA")
        ipv6 = result[0]
        return ipv6.address
    except dns.resolver.NoAnswer:
        return "No AAAA records"
    except dns.resolver.NXDOMAIN:
        return"No such domain"
```