import sqlite3
from fastapi import FastAPI

app = FastAPI()


#DATABASE SETUP 

# Connect to SQLite database file "test.db"
# If the file doesn't exist, SQLite creates it automatically
# check_same_thread=False allows the connection to be used across multiple requests
conn = sqlite3.connect("test.db", check_same_thread=False)

# Cursor is used to execute SQL commands 
cursor = conn.cursor()

# Create the todos table only if it doesn't already exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id        INTEGER PRIMARY KEY,  
        title     TEXT    NOT NULL,     
        completed TEXT    NOT NULL      
    )
""")

# commit() saves the changes permanently to the database file
conn.commit()


#Route

@app.get("/")
def home():
    return {"message": "SQLite connected"}