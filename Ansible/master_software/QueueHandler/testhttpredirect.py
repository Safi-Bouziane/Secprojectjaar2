import mysql.connector
import requests
import sys
def https(Url):
    try:
     website = requests.get(Url)
    except:
        return "check failed"
    url = website.url
    score = 1
    finished = 0

    if url.startswith(('https://')):
        return "https redirectie aanwezig."
    else:
        return"https niet redirectie aanwezig!!!"
result = https(sys.argv[1])
rowid = sys.argv[2]
if 1:
        mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="DeltaGroepPassword#",
        database="securityproject")
        mycursor = mydb.cursor()
        sql = f"UPDATE Result SET TEST1 = %s WHERE ID = %s"
        val = (result,rowid)
        mycursor.execute(sql, val)
        mydb.commit()