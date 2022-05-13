import socket
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
site = "www.facebook.com"

print (socket.gethostbyname(site), 80)