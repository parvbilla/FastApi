from fastapi import FastAPI , Depends
app=FastAPI()

def get_name():
    return "parv"

@app.get("/user")
def get_user(name : str = Depends(get_name)):
    return{
        "name":name
    }

def get_id():
    return 101

@app.get("/profile")
def get_user_id(user_id : int = Depends(get_id)):
    return{
        "user_id":user_id
    }