from fastapi import FastAPI, Response
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

mydb = mysql.connector.connect(
host="securityprojecthowsami.mysql.database.azure.com",
user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
password="Honden120",
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
    sql = "SELECT * FROM `Result` WHERE IP = '"+ip+"';"
    print(sql)
    mycursor.execute(sql)
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