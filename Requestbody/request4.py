from fastapi import FastAPI
from pydantic import BaseModel
from request3 import Model

app = FastAPI()

@app.put("/Update/{item_id}")
async def update_item(item_id:int,Item:Model):
    result = {"item_id":item_id,**Item.model_dump()}
    return result