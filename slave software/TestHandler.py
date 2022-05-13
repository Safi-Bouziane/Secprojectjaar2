import os

def startcontainers(ip,id,url,test1,test2,test3,test4,test5,test6):
    if  test1:
        os.popen(f'sudo docker run -d test1 python3 testhttpredirect.py {url} {id}')
    if  test2:
        os.popen(f'sudo docker run -d test2 python3 geoip.py {ip} {id}')
    if  test3:
        os.popen(f'sudo docker run -d test3 python3 blacklistcheck.py {url} {id}')
    if  test4:
        os.popen(f'sudo docker run -d test4 python3 sslcheck.py {url} {id}')
    if  test5:
        os.popen(f'sudo docker run -d test5 python3 dnssec_check.py {url} {id}')
    if  test6:
        os.popen(f'sudo docker run -d test6 python3 dnsipv6_check.py {url} {id}')