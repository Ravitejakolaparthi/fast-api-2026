from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel, Field
app = FastAPI()
Customers = [
    {"id": 1, "name": "Ravi", "active": True},
    {"id": 2, "name": "Teja", "active": False},
]
Orders = [
    {"id": 1, "customer_id": 1, "item": "Biriyani"},
    {"id": 2, "customer_id": 2, "item": "Pizza"},
    {"id": 3, "customer_id": 1, "item": "Fried Rice"},
]
def get_current_customer():
    for customer in Customers :
     if customer["name"] == "Ravi":
        return customer

@app.get("/myOrders")
def getMyOrders(customer = Depends(get_current_customer)):
    MyOrders = []
    for orders in Orders :
       if orders["customer_id"] == customer["id"] :
          MyOrders.append(orders)
    return MyOrders


   