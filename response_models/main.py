from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class UserResponse(BaseModel):
    name: str
    age: int
    email: str


@app.get("/user_reponse",response_model=UserResponse)
def user_response():
    return{
        "name":"parv",
        "age":21,
        "email":"parv@gmail.com",
        "password":"1234"
  }