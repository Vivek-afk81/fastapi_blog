from fastapi import FastAPI, Request

# Create the FastAPI application instance.
app = FastAPI()

# This middleware runs for every HTTP request.
@app.middleware("http")
async def my_middleware(request: Request, call_next):
    print("Request Received")  # Executed before the request reaches the route.

    # Pass the request to the next middleware or route handler.
    response = await call_next(request)

    print("Response SENT")  # Executed just before the response is returned.

    return response

# A simple endpoint for testing the middleware.
@app.get("/")
async def home():
    return {"message": "Hello, FastAPI!"}