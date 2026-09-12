from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    id:int
    name: str
    age: int
    email:str

users=[]
@app.get("/get_users")
def get_users():
    return users

@app.post("/add_user")
def add_user(user:User):
    users.append(user)
    return{
        "message":"User added successfully",
        "user":user
    }

@app.put("/update_user/{user_id}")
def update_user(user_id: int, user: User):

    for index, oneUser in enumerate(users):

        if user_id == oneUser.id:
            users[index] = user

            return {
                "message": "user updated successfully",
                "user": user
            }

    return {
        "message": "error occurred, user not updated"
    }


@app.delete("/delete_user/{user_id}")
def delete_user(user_id:int): 
    for index,oneUser in enumerate(users):
        if user_id==oneUser.id:
            delete_user=users.pop(index)
            return {"message":"user deleted successfully","user":delete_user}
        
    return{
        "message":"user id not found"
    }
        