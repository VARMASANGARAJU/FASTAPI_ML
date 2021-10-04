from fastapi import FastAPI, Body, Request, File, UploadFile, Form, Depends, BackgroundTasks
import uvicorn
import time
from pydantic  import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from fastapi.responses import StreamingResponse
import io

from typing import List

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from model_file import *

app = FastAPI()

#for Reading CSV Into Pandas
import pandas as pd
import os
from io import StringIO
import io, base64

list_of_usernames = list()
templates = Jinja2Templates(directory="htmltemplates")

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

def handle_email_background(email:str, data:str):
    print(email)
    print(data)
    for i in range(100):
        print(i)
        time.sleep(0.1)


@app.get("/users/email")
async  def handle_email(email:str, background_task: BackgroundTasks):
    print(email)
    background_task.add_task(handle_email_background,email,"THIS IS SAMPLE BACKGROUND TASK MANAGER")
    return {"user":"varma", "message":"Mail Sent"}


@app.post("/token")
async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token" :form_data.username , "toke_type" : "bearer"}


@app.get("/users/profilepic")
async def profile_pic(token:str=Depends(oauth_scheme)):
    print(token)
    return {
        "user" : "varma",
        "profile_pic" : "my_face"
    }



class NameValues(BaseModel):
    name : str = None
    country : str = None
    age : int
    base_salary : float


@app.get("/home/{user_name}", response_class=HTMLResponse)
def write_home(request: Request, user_name:str):
    return templates.TemplateResponse("home.html", {"request":request, "username": user_name})

@app.post("/submitform")
async def handle_form(assignment: str = Form(...), assignment_file: UploadFile = File(...)):
    print(assignment)
    print(assignment_file.filename)
    csv_data = pd.read_csv(assignment_file.file)
    input_data = Reader.csv_reader(csv_data)

    transform = Transformer(input_data)
    forecast = Forecast()
    final_data = forecast.run_forecast(transform.dataframe, 12)
    final_data  = final_data.to_frame().reset_index()

    stream = io.StringIO()
    final_data.to_csv(stream, index=False)

    response = StreamingResponse(iter([stream.getvalue()]),
                            media_type="text/csv"
       )

    response.headers["Content-Disposition"] = "attachment; filename=export.csv"


    return response



@app.post("/postData")
def post_data(name_value: NameValues, spousal_status: str = Body(...)):
    print(name_value)
    return {
        "usernames" : name_value.name,
        "spousal_status" : spousal_status
        }





if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1",port=8000)
