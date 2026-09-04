from sqlalchemy import create_engine, Column, Integer, String, Boolean  
from sqlalchemy.orm import sessionmaker, declarative_base, Session       
from fastapi import FastAPI, Depends                                     

app = FastAPI()


# DATABASE CONFIGURATION 

# Database URL — tells SQLAlchemy which database to use and where
# "sqlite:///./test.db" means SQLite file named test.db in the current directory
DATABASE_URL = "sqlite:///./test.db"

# Engine — the core connection to the database
# check_same_thread=False is SQLite-specific — allows use across multiple threads
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SessionLocal — a factory that creates new database sessions
# Each request gets its own session — autocommit/autoflush off by default
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base — all ORM models inherit from this
# It keeps track of all models so create_all() knows what tables to create
Base = declarative_base()


#ORM MODEL

# ORM (Object Relational Mapper) — lets you work with DB tables as Python classes
# Each attribute = one column in the database table
class Todo(Base):
    __tablename__ = "todos"                                 # actual table name in the database

    id        = Column(Integer, primary_key=True, index=True)   # auto-incremented unique ID
    title     = Column(String, nullable=False)                  # todo text, required
    completed = Column(Boolean, default=False)                  # BUG FIX: Boolean instead of String


# Creates all tables in the database if they don't already exist
# Must be called after all models are defined
Base.metadata.create_all(bind=engine)


# DEPENDENCY — DATABASE SESSION 

# get_db() is a dependency — FastAPI calls it automatically for every route that needs a DB session
# yield db → gives the session to the route
# finally  → always closes the session after the route finishes, even if an error occurs
def get_db():
    db = SessionLocal()     # open a new session for this request
    try:
        yield db            # provide session to the route
    finally:
        db.close()          # always close — prevents connection leaks


#ROUTE

# Depends(get_db) tells FastAPI to run get_db() and inject the session as `db`
# The route doesn't create the session itself — FastAPI handles it automatically
@app.get("/")
def home(db: Session = Depends(get_db)):
    return {"message": "SQLAlchemy connected"}  