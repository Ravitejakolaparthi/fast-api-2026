from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field
from Orders import router

app = FastAPI()
app.include_router(router)

# RequestBody

class MenuItem(BaseModel):
    name : str
    price : int = Field(gt = 0)
    category : str | None = None
    description : str | None = None

# ResponseBody

class MenuItemOut(BaseModel):
    id : int
    name : str
    price : int
    category : str | None = None

# Patching Body
class MenuUpdate(BaseModel):
    name : str | None = None
    price : int | None = Field(default=None,gt = 0)
    category : str | None = None
    description : str | None = None
# Replacing whole item
class MenuItemPut(BaseModel):
     name : str
     price : int = Field(gt = 0)
     category : str 
     description : str
# Data

Data = [
    {
            "id":1,
            "name":"Chicken Briniyani",
            "price": 250,
            "category" : "Non Veg"
        }
    ,
   {
            "id":2,
            "name":"Chicken Mogalai Briniyani",
            "price": 270,
            "category" : "Non Veg"
        },
    {
            "id":3,
            "name":"Veg Briniyani",
            "price": 240,
            "category" : "Veg"
    }
]

@app.post("/menu",response_model=MenuItemOut)
def add_menu(item:MenuItem):
    new_item = item.model_dump()
    new_item["id"] = len(Data)+1
    Data.append(new_item)
    return new_item
    

@app.get("/menu",response_model=list[MenuItemOut])
def Show_menu():
    return Data

@app.get("/memu/{item_id}",response_model=MenuItemOut)
def Show_item_menu(item_id:int):
    for i in Data:
        if i["id"] == item_id :
            return i
    raise HTTPException(
        status_code=404,
        detail="Menu does not contian Item"
    )
       
@app.delete("/menu/{item_id}")
def remove_item(item_id : int):
    for key,val in enumerate(Data):
        if val["id"] == item_id:
            Data.pop(key)
            return {
                "Message":"Item removed SuccesFully"
            }
    raise HTTPException(
        status_code=404,
        detail="Not Found"
    )

@app.patch("/menu/{item_id}",response_model=list[MenuItemOut])
def Update_item(item_id:int,item:MenuUpdate):
        for val in Data:
            if val["id"] == item_id :
                data = item.model_dump(exclude_unset=True)
                val.update(data)
                return Data
        raise HTTPException(
            status_code=404,
            detail="Not found"
        )
@app.put("/menu/{item_id}",response_model=MenuItemOut)
def Replace_item(item_id : int,item : MenuItemPut):
        for i in Data:
             if i["id"] == item_id :
                  data=item.model_dump()
                  i.update(data)
                  return i
        raise HTTPException(
             status_code=404,
             detail="Not Found"
        )    

# Orders_API
#===================================================================================================================
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
@app.post("/orders",response_model=OrderOut)
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

@app.get("/orders",response_model=list[OrderOut])
def show_orders():
     return Orders

@app.get("/orders/{order_id}",response_model=OrderOut)
def show_order_with_id(order_id:int):
     for val in Orders:
          if val["id"] == order_id:
               return val
     raise HTTPException(
          status_code=404,
          detail="Not Found"
     )
@app.patch("/order/{order_id}",response_model=OrderOut)
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
    
@app.delete("/orders/{order_id}",response_model=OrderOut)
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


          