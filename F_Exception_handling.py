from fastapi import FastAPI, HTTPException, Request   # Request needed for exception handlers
from fastapi.responses import JSONResponse            # used to return custom JSON error responses

app = FastAPI()


# Built in http exception

# HTTPException is FastAPI's built-in way to return standard HTTP errors
# status_code sets the HTTP status, detail sets the error message
@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,        # 404 = resource not found
            detail="User not found" # message returned in the JSON response
        )
    return {
        "id": 1,
        "name": "Vivek"
    }


# Custom Exception 

# Step 1: Define a custom exception class by inheriting from Python's base Exception
# Useful when you want more control over error structure and messaging
class UserNotFoundException(Exception):
    def __init__(self, name):
        self.name = name    # stores the name so the handler can use it in the message


# Step 2: Register a global exception handler using @app.exception_handler()
# This function is called automatically whenever UserNotFoundException is raised ANYWHERE in the app
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):
    # request → the incoming HTTP request (required by FastAPI, even if unused)
    # exc     → the actual exception instance, gives access to exc.name
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User '{exc.name}' not found"   # dynamic message using the raised exception's data
        }
    )


# Step 3: Raise the custom exception in any route — handler catches it globally
# Example: GET /custom_error_user/mohit  → triggers UserNotFoundException
@app.get("/custom_error_user/{name}")
def get_custom_error_user(name: str):
    if name != "vivek":
        raise UserNotFoundException(name)   # caught by user_not_found_handler automatically
    return {
        "name": name
    }