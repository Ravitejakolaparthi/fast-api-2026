from fastapi import FastAPI
from pydantic import BaseModel

class Model(BaseModel):
    id : int = 1
    name : str
    age : int
    income : int
    spend : int
    saving : int

app = FastAPI()

@app.post("/Update/")
async def Update_details(Person:Model):
        temp = Person.model_dump()
        Person.saving = Person.income - Person.spend
        temp.update({"saving":+Person.saving})
        return temp

        