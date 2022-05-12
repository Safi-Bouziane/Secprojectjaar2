import socket
import ssl
import certifi

def ssl_check(url):
    context=ssl.create_default_context(cafile=certifi.where())
    if url.startswith(('http://')):
        hostname = url[7:]
    elif url.startswith(('https://')):
        hostname = url[8:]
    else:
        hostname = url
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return ssock.version()
