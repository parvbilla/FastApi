from fastapi import FastAPI, Request
from mockData import product

app=FastAPI()

@app.get("/")
def home():
    return {"welcome to fastapi series!"}


@app.get("/contact")
def contact():
    return {"welcome to contact page"}

@app.get("/products")
def products():
    return product

@app.get("/product/{product_id}")
def getOneProduct(product_id:int):
    for Oneproduct in product:
        if Oneproduct.get("id") == product_id:
            return Oneproduct

    return {"error":"product not found"}

#query params

@app.get("/greet")
def greet(request:Request):
    query_params=dict(request.query_params)
    print(query_params)
    return{
        "greet":f"hello {query_params.get('name')} you age is {query_params.get('age')}"
    }


