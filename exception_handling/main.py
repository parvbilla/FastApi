from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/user/{user_id}")
def get_user(user_id: int):

    if user_id != 2:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": 2,
        "name": "Parv"
    }


class MyException(Exception):
    pass


@app.exception_handler(MyException)
async def my_exception_handler(request: Request, exc: MyException):

    return JSONResponse(
        status_code=400,
        content={
            "message": "This is my custom exception"
        }
    )


@app.get("/custom")
def custom_error():

    raise MyException()


@app.exception_handler(Exception)
async def global_error_handler(request: Request, exc: Exception):

    return JSONResponse(
        status_code=500,
        content={
            "message": "Something went wrong"
        }
    )


@app.get("/error")
def error():

    result = 10 / 0

    return {
        "result": result
    }