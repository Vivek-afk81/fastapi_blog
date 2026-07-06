from fastapi import FastAPI, status, HTTPException

app=FastAPI()

@app.post("/create_user",status_code= status.HTTP_201_CREATED)
def create_user():
    return{
        "message":"user_created"
    }


#custom response
@app.get("/user")
def get_user():
    return{
        "status":"success",
        "message":"User fetched",
        "data":{
            "name":"Vivek",
            "age":"21",
        }
    }

# basic error handling

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return {
        "id":1,
        "name":"Vivek"
    }