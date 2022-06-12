import dns.resolver
import sys
import mysql.connector

# domain = "https://vrt.be"

def spf(url):
    domain = url
    if domain.startswith(('http://')):
        domain = domain[7:]
    elif domain.startswith(('https://')):
        domain = domain[8:]
    else:
        domain = domain

    try:
        result = dns.resolver.resolve(domain, 'TXT')
        for record in result:
            if 'spf1' in str(record):
                return record
        return "No SPF record"
    except dns.resolver.NXDOMAIN:
        return "Domain not found"

result = spf(sys.argv[1])
rowid = sys.argv[2]
# print(result)

if 1:
        mydb = mysql.connector.connect(
        host="secproject.mysql.database.azure.com",
        user="testuser@secproject.mysql.database.azure.com",
        password="DeltaGroepPassword#",
        database="securityproject")
        mycursor = mydb.cursor()
        sql = f"UPDATE Result SET TEST7 = %s WHERE ID = %s"
        val = (result,rowid)
        mycursor.execute(sql, val)
        mydb.commit()