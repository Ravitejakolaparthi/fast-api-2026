from fastapi import FastAPI,Cookie
from typing import Annotated
app = FastAPI()
@app.post("/session")
async def read_det(login_id : Annotated[str,Cookie()]):
    return {"login_id" : login_id}

