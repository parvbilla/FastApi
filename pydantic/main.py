from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str


@app.post("/create_user")
def create_user(user:User):
    return {
    "message":"User created successfully",
    "data":user
    }

# nested model

class Address(BaseModel):
    city:str
    state:str
    pincode:int

class Users(BaseModel):
    name:str
    age:int
    email:str
    address:Address


@app.post("/create_users")
def create_users(users:Users):
    return{
        "message":"users created successfully...",
        "data":users
    }
