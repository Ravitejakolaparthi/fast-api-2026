from fastapi import FastAPI,Query
from typing import Annotated
app = FastAPI()
@app.get("/items")
async def read_items(q: Annotated[str,Query(
    title="My learn",
    description="To do something using this",
    min_length=3
    
)]):
    return q