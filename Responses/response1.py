from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class item(BaseModel) :
    id : str
    name : str
@app.post("/items")
async def get_items(itm : item) -> item:
    return itm

@app.get("/items")
async def read_items() -> list[item]:
    return [
        item(id="132",name="nifbsif"),
        item(id="213",name="sfihbrsif")
    ]