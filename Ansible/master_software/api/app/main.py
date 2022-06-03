from fastapi import FastAPI,BackgroundTasks,File, UploadFile, Body, Depends
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from subprocess import Popen

from model import PostSchema, UserSchema, UserLoginSchema
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT

users = []

import mysql.connector
from mysqlInsert import *

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

app = FastAPI()


@app.post("/add/", dependencies=[Depends(JWTBearer())])
async def read_user_item(item: Resultaat):
    InsertIntoQueue(item.ip,item.url,item.test1,item.test2,item.test3,item.test4,item.test5,item.test6)
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
