from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    # CORSMiddleware running before any request
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
redis = get_redis_connection(
    host="redis-18308.c15.us-east-1-4.ec2.cloud.redislabs.com",
    port=18308,
    password="sPmD5CXarczYMF0KEKlwrbH0M1MLdZcq",
    decode_responses=True
)


class Product(HashModel):
    name: str
    price: float
    quantity: int

    # to connect Product model with redis database which is a realtime database
    class Meta:
        database = redis


@app.get("/product")
def Get_data():
    return [formate(pk) for pk in Product.all_pks()]


def formate(pk: str):
    product = Product.get(pk)
    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "qunatity": product.quantity
    }


@app.post("/product")
def create(product: Product):
    return product.save()


@app.get("/product/{pk}")
def get_single_data(pk: str):
    return Product.get(pk)


@app.delete("/product/{pk}")
def Delete_data(pk: str):
    return Product.delete(pk)
