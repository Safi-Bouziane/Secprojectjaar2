FROM python:latest
#voor queuecontainer
COPY requirements.txt etc/requirements.txt
COPY testHandler.py ./
COPY queueHandler.py ./
RUN pip install -r etc/requirements.txt
RUN pip install python-multipart
CMD ["python3", "queueHandler.py"]

#voor httphttps te builden
RUN pip3 install requests
#voor met mysql resulthandeler
#run pip3 install mysql-connector-python

#vr geoip te builden
RUN pip3 install maxminddb 
RUN pip3 install maxminddb-geolite2

#vr blacklist
RUN pip3 install git+https://github.com/rthalley/dnspython
RUN pip3 install urllib3
RUN pip3 install requests

#vr dnsipv6
RUN pip3 install dnspython

#ssl,dnssec en shodan hebben niks nodig




COPY shodancheck.py ./
COPY blacklistcheck.py ./
COPY geoip.py ./
COPY dnsipv6_check.py ./
COPY dnssec_check.py ./
COPY sslcheck.py ./
COPY testhttpredirect.py ./
COPY queueHandler.py ./
#verander hier voor andere testen om zo een docker image te maken vr die test