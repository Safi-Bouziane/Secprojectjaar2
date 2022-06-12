from fastapi import FastAPI, Response
import mysql.connector
from pydantic import BaseModel

app = FastAPI(openapi_url = "/resulhandleropenapi.json")

mydb = mysql.connector.connect(
host="secproject.mysql.database.azure.com",
user="argususer",
password="DeltaGroepPassword#",
database="securityproject")
class verify(BaseModel):
    ip: str
    verify: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/result/{ip}")
async def read_item(ip):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM `Result` WHERE IP = IP VALUES(IP);"
    val = (ip)
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    return {"message": result}

@app.post("/verify/", status_code = 200)
async def read_item(item: verify):
    if item.verify == 'true':
        mycursor = mydb.cursor()
        sql = f"DELETE FROM `Result` WHERE ip = '{item.ip}';"
        mycursor.execute(sql)
        mydb.commit()
    return "ok"


#/***************************************************************
#*
#* Copyright (Wouter Weemaes, Safi Bouziane, Kamil Grielens, Robbe Willeme) - All rights reserved. 
#*
#* Unauthorized use, copy, modify, merge, publish, distribute, sublicense, 
#* and/or sell any parts of the software/source code is strictly prohibited.
#* Proprietary and confidential
#* License: No license. 
#* Written by: (Wouter Weemaes) (wouterweemaes@outlook.com), (06/2022)
#*
#****************************************************************/
