from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

#create API
@app.post("/todos")
def create_to_dos(todo:Todo):
    todos.append(todo)
    return {"message" : "TO-DO added","data":todo }

#get API
@app.get("/todos")
def get_to_dos():
    return todos

@app.get("/todos/{todo_id}")
def get_to_do(todo_id:int):
    for todo in todos:
        if todo.id ==todo_id:
            return todo
    return {"error":"Todo not found"}

#update todos
@app.put("/todos/{todo_id}")
def update_to_do(todo_id:int,updated_todo:Todo):
    for idx,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[idx]=update_to_do
            return {
                "message":"Data Uploaded",
                "data":update_to_do
            }
    return {"error":"not found"}