from fastapi import FastAPI,BackgroundTasks,File, UploadFile
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from subprocess import Popen
import psutil
from TestHandler import StartTests

class input(BaseModel):
    ip: str
    url: str
    id: str
    test1: bool
    test2: bool
    test3: bool
    test4: bool
    test5: bool
    test6: bool

app = FastAPI()

@app.get("/cpuload")
async def root():
    return psutil.cpu_percent()

@app.post("/add/", status_code = 200)
async def read_user_item(item: input):
    StartTests(item.ip,item.url,item.id,item.test1,item.test2,item.test3,item.test4,item.test5,item.test6)
    return "ok"
