from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class item(BaseModel):
    name : str
    age : int
@app.get("/item/")
async def get_det(Item : item):
        temp_Item= Item.model_dump()
        return temp_Item
        