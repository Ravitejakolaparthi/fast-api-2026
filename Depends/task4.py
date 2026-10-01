from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
app = FastAPI()
Customers = [
    {"id": 1, "name": "Ravi", "active": True},
    {"id": 2, "name": "Teja", "active": True},
    {"id": 3, "name": "Sai", "active": False},
]

Orders = [
    {"id": 1, "customer_id": 1, "item": "Chicken Biryani"},
    {"id": 2, "customer_id": 2, "item": "Veg Biryani"},
    {"id": 3, "customer_id": 1, "item": "Fried Rice"},
    {"id": 4, "customer_id": 3, "item": "Chicken Biryani"},
]



def get_current_customer(name : str):
    for customer in Customers:
       if customer["name"] == name:
        return customer
    raise HTTPException(
         status_code=404,
         detail="customer Not Found"
    )
def check_activity_of_customer(customer=Depends(get_current_customer)):
        if customer["active"] == True:
             return customer
        else :
             raise HTTPException(
                  status_code=404,
                  detail="Customer Not in Active"
             )
@app.get("/my_orders/{name}")
def get_customer_orders(name:str,customer=Depends(check_activity_of_customer)):
            item_list = []
            for Order in Orders :
                if Order["customer_id"] == customer["id"] : 
                    item_list.append(Order)
            return item_list