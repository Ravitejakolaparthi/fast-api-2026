from fastapi import FastAPI,Cookie
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()
class COOKIE(BaseModel):
    name : str
    id : int
    passowrd : str
@app.post("CookieSeeson")
async def Cookies(cokie : Annotated [COOKIE,Cookie()]):
    return cokie