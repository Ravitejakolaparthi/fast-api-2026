from fastapi import FastAPI,Query
from typing import Annotated


app = FastAPI()
@app.get("/items")
async def read_items(q:Annotated[list[str],Query()]):
    return {"q":q}
