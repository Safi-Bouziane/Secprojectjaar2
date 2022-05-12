import socket
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
site = "http://www.facebook.be"

socket.gethostbyname(site), 80