from fastapi import FastAPI,BackgroundTasks,File, UploadFile, Body, Depends
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from subprocess import Popen
from model import PostSchema, UserSchema, UserLoginSchema
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
users = []

import mysql.connector

def InsertIntoQueue(IP, RESULT, TEST1, TEST2, TEST3, TEST4, TEST5, TEST6, TEST7, TEST8):
    mydb = mysql.connector.connect(
    host="secproject.mysql.database.azure.com",
    user="argususer",
    password="DeltaGroepPassword#",
    database="securityproject"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO `queue`(IP,URL,TEST1,TEST2,TEST3,TEST4,TEST5,TEST6, TEST7, TEST8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    val = (IP, RESULT, TEST1, TEST2, TEST3, TEST4, TEST5, TEST6, TEST7, TEST8)
    mycursor.execute(sql, val)
    mydb.commit()
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False
class Resultaat(BaseModel):
    ip: str
    url: str
    test1: bool
    test2: bool
    test3: bool
    test4: bool
    test5: bool
    test6: bool
    test7: bool
    test8: bool
app = FastAPI()
@app.post("/add/", dependencies=[Depends(JWTBearer())])
async def read_user_item(item: Resultaat):
    InsertIntoQueue(item.ip,item.url,item.test1,item.test2,item.test3,item.test4,item.test5,item.test6, item.test7, item.test8)
    return "ok"
@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)
@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }




# https://testdriven.io/blog/fastapi-jwt-auth/

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
