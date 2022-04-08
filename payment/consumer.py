import time
from fastapi import FastAPI
from main import redis,Order

app = FastAPI()
key = "refund_order"
group = "payment-group"

try:
    redis.xgroup_create(key, group)
except:
    print("Group Already Exist!")

while True:
    try:
        result = redis.xreadgroup(group, key, {key: ">"}, None)
        if result != []:
            print("result:",result)
            for res in result:
                obj = res[1][0][1]
                order = Order.get(obj["pk"])
                order.status ="refunded"
                print("AfterDeleteingOrder",order)
                order.save()

    except Exception as error:
        print(str(error))
    time.sleep(1)
