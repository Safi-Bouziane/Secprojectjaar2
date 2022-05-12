import os
from tqdm import tqdm        
import time
import psutil
import mysql.connector


def checkdb():
    mydb = mysql.connector.connect(
        host="securityprojecthowsami.mysql.database.azure.com",
        user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
        password="Honden120",
        database="securityproject"
)
    mycursor = mydb.cursor()
    mycursor.execute("select count(*) from queue")  
    myresult=mycursor.fetchone()
    if myresult[0] <= 0:
        print ("This table is empty!")
        mycursor.close()
        mydb.close()
        time.sleep(3)
        return myresult[0]
    else:
        mycursor.close()
        mydb.close()
        return myresult[0]
        
while 1:
    wait = checkdb()
    while wait != 0:    
        with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
            for x in range(wait):
                rambar.n=psutil.virtual_memory().percent
                cpubar.n=psutil.cpu_percent()
                rambar.refresh()
                cpubar.refresh()
                if cpubar.n < 80 and rambar.n < 80:
                    os.popen(f'sudo docker run -d queue')
                else:
                    time.sleep(3)
        wait = checkdb()
    