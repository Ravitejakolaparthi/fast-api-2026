from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Body(BaseModel):
    name :str
    age: int
class Person(BaseModel):
    id : int
    branch : str

@app.post("/body")
async def getbody(bdy : Body,Per : Person):
    return {"body":bdy,"person":Per}