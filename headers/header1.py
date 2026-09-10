from fastapi import FastAPI,Header
from typing import Annotated
from pydantic import BaseModel
app =  FastAPI()


@app.get("/head")
async def get_head(det : Annotated[str,Header()]):
    return det