import time

from fastapi import FastAPI

from main import redis, Product

app = FastAPI()
key = "order_completed"
group = "inventory-group"

try:
    redis.xgroup_create(key, group)
except:
    print("Group Already Exist!")

while True:
    try:
        result = redis.xreadgroup(group, key, {key: ">"}, None)
        if result != []:
            for res in result:
                obj = res[1][0][1]
                try:
                    product = Product.get(obj["product_id"])
                    print(product)
                    print("product", product)
                    product.quantity = product.quantity - int(obj["quantity"])
                    product.save()
                except:
                    redis.xadd("refund_order", obj, "*")

    except Exception as error:
        print(str(error))
    time.sleep(1)
