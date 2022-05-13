import sys
import urllib.request
import mysql.connector
def dnscheck(Url):
                results = urllib.request.urlopen('http://portfolio.sidnlabs.nl/check/%s' % Url).read()
                newResults = results.decode('utf-8').split()
                finalResult = newResults[0].replace(Url, '').replace(',', '')
                return Url + " is " + finalResult + " with DNSSEC."
result = dnscheck(sys.argv[1])
rowid = sys.argv[2]
if 1:
        mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="Honden120",
        database="securityproject")
        mycursor = mydb.cursor()
        sql = f"UPDATE Result SET TEST5 = %s WHERE ID = %s"
        val = (result,rowid)
        mycursor.execute(sql, val)
        mydb.commit()