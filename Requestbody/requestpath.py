from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class items(BaseModel):
    name : str
    id : int

@app.post("/item/{item_id}")
async def get_det(item_id :int ,Item : items):
    return {"item_id":item_id,"item":Item}   
