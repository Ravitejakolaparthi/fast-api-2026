from fastapi import APIRouter,HTTPException
from pydantic import BaseModel, Field


router=APIRouter()

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

@router.post("/menu",response_model=MenuItemOut)
def add_menu(item:MenuItem):
    new_item = item.model_dump()
    new_item["id"] = len(Data)+1
    Data.append(new_item)
    return new_item
    

@router.get("/menu",response_model=list[MenuItemOut])
def Show_menu():
    return Data

@router.get("/memu/{item_id}",response_model=MenuItemOut)
def Show_item_menu(item_id:int):
    for i in Data:
        if i["id"] == item_id :
            return i
    raise HTTPException(
        status_code=404,
        detail="Menu does not contian Item"
    )
       
@router.delete("/menu/{item_id}")
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

@router.patch("/menu/{item_id}",response_model=list[MenuItemOut])
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
@router.put("/menu/{item_id}",response_model=MenuItemOut)
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