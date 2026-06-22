from fastapi import FastAPI

# Create the FastAPI app instance — this is the core of your API
app = FastAPI()


#STATIC ROUTES

# @app.get() registers a GET route; "/" is the root/homepage of the API
@app.get("/")
def home():
    return {"message": "Rasmalai"}


# A second static route — URL is fixed, always returns the same response
@app.get("/faq")
def faq():
    return {"FAQs": "Frequently asked questions"}


#PATH PARAMETERS (Dynamic Routes)

# {post_id} is a path parameter — part of the URL itself
# Example request: GET /posts/42  →  post_id = 42
@app.get("/posts/{post_id}")
def get_post(post_id: int):   # type hint `int` tells FastAPI to validate & convert automatically
    return {"post_id": post_id}


# QUERY PARAMETERS
# Query params come after "?" in the URL, e.g. /users?name=Mohit
# They are defined as regular function arguments (NOT inside the URL path)

# Optional query parameter — defaults to None if not provided
# Example: GET /users?name=Mohit  or  GET /users  (name will be None)
@app.get("/users")
def get_users(name: str = None):
    return {"name": name}


# Query parameter with a default value
# Example: GET /products→ limit = 10  (default)
#          GET /products?limit=5→ limit = 5
@app.get("/products")
def get_products(limit: int = 10):   # type int added for proper validation
    return {"limit": limit}


# Multiple query parameters — all optional, each with its own default
# Example: GET /items?name=Chair&price=500
@app.get("/items")
def get_items(name: str = None, price: int = 10):
    return {
        "name": name,
        "price": price   # 
    }

# REQUEST BODY
# Unlike GET,in POST the data travels in the request BODY, not the URL
# POST route — cannot be tested directly in browser; use Swagger UI at /docs

@app.post("/create-user")
def create_user(user: dict):  # accepts any JSON object as a plain dict — flexible but NO validation
    # FastAPI automatically reads the JSON body and passes it as `user`
    # Downside of dict: no type checking, no required fields, no error messages
    return {
        "message": "User created",
        "data": user            # echoes back whatever JSON was sent
    }