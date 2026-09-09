from fastapi import FastAPI, Request
from mockData import product
from dtos import ProductDTO

app=FastAPI()

@app.get("/")
def home():
    return {"welcome to fastapi series!"}


@app.get("/contact")
def contact():
    return {"welcome to contact page"}

@app.get("/product")
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


@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data=product_data.model_dump()
    product.append(product_data)
    return{"message":"product created successfully","data":product}


@app.put("/update_product/{product_id}")
def update_product(product_data: ProductDTO, product_id: int):

    product_data = product_data.model_dump()

    for index, oneProduct in enumerate(product):

        if oneProduct.get("id") == product_id:

            product[index] = product_data

            return {
                "message": "Product updated successfully...",
                "product_data": product_data
            }

    return {
        "message": "Product ID does not exist for this product"
    }



@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index , oneProduct in enumerate(product):
        if(oneProduct.get("id")==product_id):
            delete_product=product.pop(index)
            return{"message":"product deleted successfully...","product":delete_product}
        
    
    return{
        "message":"product id not found"
    }