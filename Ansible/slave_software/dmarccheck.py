import dns.resolver
import sys
import mysql.connector


# domain = "google.com"

def dmarc(url):
    domain = url
    if domain.startswith(('http://')):
        domain = domain[7:]
    elif domain.startswith(('https://')):
        domain = domain[8:]
    else:
        domain = domain

    try:
        result = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
        for record in result:
            if 'DMARC1' in str(result):
                return record
        return "No DMARC record"
    except dns.resolver.NXDOMAIN:
        return "Domain not found"

result = dmarc(sys.argv[1])
rowid = sys.argv[2]
# print(result)

if 1:
        mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="DeltaGroepPassword#",
        database="securityproject")
        mycursor = mydb.cursor()
        sql = f"UPDATE Result SET TEST8 = %s WHERE ID = %s"
        val = (result,rowid)
        mycursor.execute(sql, val)
        mydb.commit()