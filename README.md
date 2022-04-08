# Microservices_with_fastapi

I build Microservices with fastpai 
I used redis which is realtime database

Microservice 1:
        I build inventory Microsevice which maintain our stack.
        
Microservice 2:
        I build another Microservice which is the payment Microserice.

Explanation:
          These 2 Microservices are communicate with each other through internall API call
          inventory microservice maintian our stack, when someone order any of the product and
          also specified the quantity means how many product they want to order.
          Payment microservice first internall call to the inventory microservice and see amount
          of the product , if amount of the product is equll or greater then costumer order then condition
          is statisfied and we pop of message Your order has been successfully submitted
          if costumer order is greater then remaing the product in our stack then we pop of message Sorry we
          have insufficient stack
