# SSL version check

## Bedoeling van de check
Bij deze check wordt er nagekeken welke versie van SSL/TLS wordt gebruikt.

## Werking van de code
Voor de test hebben we volgende libraries nodig.
```
import socket
import ssl
import certifi
```

In volgend stuk code halen we de correcte hostname op.
```
if url.startswith(('http://')):
        hostname = url[7:]
    elif url.startswith(('https://')):
        hostname = url[8:]
    else:
        hostname = url
```

Vervolgens kijken we na welke versie van SSL/TLS er wordt gebruikt.
```
context=ssl.create_default_context(cafile=certifi.where())
with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return ssock.version()
```