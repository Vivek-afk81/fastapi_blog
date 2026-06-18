from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


app=FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

templates=Jinja2Templates(directory="templates") 


posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]


@app.get("/",include_in_schema=False) #home route
@app.get("/posts",include_in_schema=False) #we can stack the decorators,so multiple routes can use same function here home
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
         {"posts":posts,"title":"Home"})

#Place holders as layout.html already expects these page

@app.get("/login", name="login_page")
def login_page(request: Request):
    return HTMLResponse("<h1>Login Page</h1>")

@app.get("/register", name="register_page")
def register_page(request: Request):
    return HTMLResponse("<h1>Register Page</h1>")

@app.get("/account", name="account_page")
def account_page(request: Request):
    return HTMLResponse("<h1>Account Page</h1>")

@app.get("/api/posts")
def get_posts():
    return posts 

