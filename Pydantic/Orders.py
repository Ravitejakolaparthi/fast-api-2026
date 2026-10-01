
# Orders_API
#===================================================================================================================
from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,Field
router = APIRouter()
class OrderItem(BaseModel):
    menu_item_id : int
    quantity : int = Field(gt = 0)
class Order(BaseModel):
    customer_name : str
    items : list[OrderItem]
class OrderOut(BaseModel):
    id : int
    customer_name : str
    items : list[OrderItem]
    total_price : int
class OrderUpdate(BaseModel):
     customer_name : str  | None = None
@router.post("/orders",response_model=OrderOut)
def CreateOrder(order:Order):
     total_price = 0
     for val in order.items:
         id = val.menu_item_id
         q = val.quantity
         for i in Data :
              if i["id"] == id :
                   total_price += i["price"]*q
     new_order = {
              "id" : len(Orders)+1,
              "customer_name" : order.customer_name,
              "items":order.items,
              "total_price":total_price
         } 
     Orders.append(new_order)
     return new_order

@router.get("/orders",response_model=list[OrderOut])
def show_orders():
     return Orders

@router.get("/orders/{order_id}",response_model=OrderOut)
def show_order_with_id(order_id:int):
     for val in Orders:
          if val["id"] == order_id:
               return val
     raise HTTPException(
          status_code=404,
          detail="Not Found"
     )
@router.patch("/order/{order_id}",response_model=OrderOut)
def Update_order(order_id:int,Updetails:OrderUpdate):
     for order in Orders :
        if  order["id"] == order_id :
             data = Updetails.model_dump(exclude_unset=True)
             order.update(data)
             return order
     raise HTTPException(
         status_code=404,
         detail="Not Found"
    )            
    
@router.delete("/orders/{order_id}",response_model=OrderOut)
def Remove_order(order_id:int):
     for key , val in enumerate(Orders):
          if val["id"] == order_id :
               Orders.pop(key)
               return val
     raise HTTPException(
          status_code=404,
          detail="Not Found"
     )
Orders = [
    {
        "id": 1,
        "customer_name": "Ravi",
        "items": [
            {
                "menu_item_id": 1,
                "quantity": 2
            }
        ],
        "total_price": 500
    },
    {
        "id":2,
        "customer_name":"Teja",
        "items":[
            {
                "menu_item_id":1,
                "quantity":3
            }
        ],
        "total_price":750
    },
    {
        "id":3,
        "customer_name":"sai",
        "items":[
            {
                "menu_item_id":2,
                "quantity":2
            }
        ],
        "total_price":540
    }
]


