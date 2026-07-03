from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos=[] # In-memory "database" — resets every time the server restarts

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
# PUT—replaces the entire todo object matched by id with the new one
# Requires the full Todo body in the request (all fields must be provided)
@app.put("/todos/{todo_id}")
def update_to_do(todo_id:int,updated_todo:Todo):
    for idx,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[idx]=updated_todo
            return {
                "message":"Data Uploaded",
                "data":updated_todo
            }
    return {"error":"not found"}

#delete api
@app.delete("/todos/{todo_id}")
def delete_to_do(todo_id:int):
    for idx,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(idx)
            return {"message":"data deleted"}
    return {"error":"TODO NOT FOUND"}