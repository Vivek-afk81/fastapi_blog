from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time

app = FastAPI()

# MIDDLEWARE

# Middleware intercepts EVERY request before it reaches a route
# and EVERY response before it goes back to the client
# We can think of it as a checkpoint that wraps around all our routes

#MIDDLEWARE 1 — General Request/Response Logger 

#Logs method, URL, and total processing time for every request
#Also injects a custom header "X-Process-Time" into every response

# @app.middleware("http") registers this function as an HTTP middleware
@app.middleware("http")
async def my_middleware(request: Request, call_next):

    #BEFORE the route runs 
    print("Request received")
    print(f"  Method : {request.method}")   # e.g GET,POST
    print(f"  URL    : {request.url}")      # full URL of the request

    start_time = time.time()                    

    # call_next() passes the request forward to the actual route handler
    # without this line, the request never reaches our route
    response = await call_next(request)        

    # AFTER the route runs 
    duration = time.time() - start_time
    print(f"  Response sent | Time taken: {duration:.4f}s")

    # Attach processing time as a custom response header
    response.headers["X-Process-Time"] = str(duration)
    return response


# MIDDLEWARE 2 — Path-Specific Logger 

# A lighter middleware that logs only the route path and time taken
# Useful to show that multiple middleware can coexist and stack
@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)         # passes to next middleware or route
    process_time = time.time() - start_time
    print(f"Path:{request.url.path} | Time:{process_time:.4f}s")
    return response


#ROUTE 

# Simple route to test both middleware 
async def home():
    return {"message": "Hello, FastAPI!"}