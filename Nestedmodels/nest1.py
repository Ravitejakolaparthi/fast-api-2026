from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class item(BaseModel) :
    item_id : int
    item_name : str
class items(BaseModel) :
    id :int
    item_count : dict[int,int] = {"item_id":"item_count"}
    item_det : item
@app.post("/items")
async def get_items(ITEMS : items):
    return ITEMS
