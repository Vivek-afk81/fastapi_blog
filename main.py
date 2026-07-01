from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

to_dos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

#create API
@app.post("/to_dos")
def create_to_dos(todo:Todo):
    to_dos.append(todo)
    return {"message" : "TO-DO added","data":todo }

#get API
app