from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()
class MenuItem(BaseModel):
    name :str
    price : int = Field(gt=0)
    category : str | None = None
    description: str |None = None
class MenuItemOut(BaseModel):
    id : int
    name : str
    price : int = Field(gt=0)
    category : str | None = None

@app.post("/menu")
def Update_Menu(Item:MenuItem):
    return Item

@app.get("/menu",response_model=MenuItemOut)
def out_menu():
    return {
        "id": "id",
        "name" : "name",
        "price" : "price",
        "category" : "category"
    }
