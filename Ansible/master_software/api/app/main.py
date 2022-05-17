from fastapi import FastAPI,BackgroundTasks,File, UploadFile
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from subprocess import Popen

import mysql.connector
mydb = mysql.connector.connect(
  host="securityprojecthowsami.mysql.database.azure.com",
  user="safidesafi@securityprojecthowsami.mysql.database.azure.com",
  password="DeltaGroepPassword#",
  database="securityproject"
)
def InsertIntoQueue(IP, RESULT, TEST1, TEST2, TEST3, TEST4, TEST5, TEST6):
    mycursor = mydb.cursor()
    sql = "INSERT INTO `queue`(IP,URL,TEST1,TEST2,TEST3,TEST4,TEST5,TEST6) values(%s,%s,%s,%s,%s,%s,%s,%s);"
    val = (IP, RESULT, TEST1, TEST2, TEST3, TEST4, TEST5, TEST6)
    mycursor.execute(sql, val)

    mydb.commit()


class Resultaat(BaseModel):
    ip: str
    url: str
    test1: bool
    test2: bool
    test3: bool
    test4: bool
    test5: bool
    test6: bool

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add/", status_code = 200)
async def read_user_item(item: Resultaat):
    InsertIntoQueue(item.ip,item.url,item.test1,item.test2,item.test3,item.test4,item.test5,item.test6)
    return "ok"

@app.post("/uploadfile/")
async def create_upload_file(uploaded_file: UploadFile):
    file_location = f"/home/azureuser/project/QueueHandler/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}

##@app.get("/{param}")
##def read_user_item(url: str):
    ##Popen('python3 ' + url, shell=True)
    ##return "ok"

