from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def logging_middleware(request: Request, call_next):

    print("Request received:", request.url.path)

    response = await call_next(request)

    print("Response status:", response.status_code)

    return response


@app.get("/")
def home():
    return {
        "message": "Hello World"
    }


@app.get("/user")
def user():
    return {
        "name": "Parv"
    }