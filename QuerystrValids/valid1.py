from typing import Annotated
from fastapi import FastAPI , Query
app = FastAPI()
@app.get("/items/")
async def read_items(q : Annotated[str | None , Query(max_length=50)] = None):
    results = [{"item1":"po"},{"item2":"pi"}]
    return results
    