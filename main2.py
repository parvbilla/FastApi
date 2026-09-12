#  data validation with pydantic models
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class user(BaseModel):
    name:str
    age:int

@app.post("/create_user")
def create_user(user:user):
    return{
        "message":"user created successfully...",
        "data":user
    }