from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


# 1. HTTP Status Code
@app.get("/success", status_code=200)
def success():
    return {"message": "Success"}


# 2. Custom Response
@app.get("/custom-response")
def custom_response():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Custom response",
            "status": "success"
        }
    )


# 3. Error Handling
@app.get("/user/{user_id}")
def get_user(user_id: int):

    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": 1,
        "name": "Mohit"
    }