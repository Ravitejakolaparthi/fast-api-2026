from fastapi import FastAPI
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def minlen(id : int):
    if len(id) > 20:
        raise ValueError("Invalid ID Format!") 
    return id
@app.get("/items")
async def get_id(id : Annotated[int,AfterValidator(minlen)]) :
    if id :
        idn = data.get(id)
    return {"id":id,"name":idn}
