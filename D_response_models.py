from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str
    password:str

class UserResponse(BaseModel):
    name:str
    age:int
    email:str

@app.get("/user",response_model=UserResponse)
def get_user():
    return{
        "name":"Vivek",
        "age":21,
        "email":"notmyday@gmail.com",
        "password":"qwertyuiop"
    }    