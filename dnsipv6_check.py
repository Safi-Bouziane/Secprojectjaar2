import sys
import dns.resolver
import mysql.connector
def ipv6(url):
    my_resolver = dns.resolver.Resolver()
    domain = url
    if domain.startswith(('http://')):
            domain = domain[7:]
    elif domain.startswith(('https://')):
            domain = domain[8:]
    else:
        domain = domain
    try:
        result = my_resolver.resolve(domain, "AAAA")
        ipv6 = result[0]
        return ipv6.address
    except dns.resolver.NoAnswer:
        return "No AAAA records"
    except dns.resolver.NXDOMAIN:
        return"No such domain"

result = ipv6(sys.argv[1])
rowid = sys.argv[2]

if 1:
        mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="Honden120",
        database="securityproject")
        mycursor = mydb.cursor()
        sql = f"UPDATE Result SET TEST6 = %s WHERE ID = %s"
        val = (result,rowid)
        mycursor.execute(sql, val)
        mydb.commit()
