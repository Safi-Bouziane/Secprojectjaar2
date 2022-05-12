import socket
import ssl
import sys

def ssl_check(url):
    context = ssl.create_default_context()
    if url.startswith(('http://')):
        hostname = url[7:]
    elif url.startswith(('https://')):
        hostname = url[8:]
    else:
        hostname = url
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return ssock.version()
website = "https://www.ap.be"
print(website)
print(ssl_check(website))
