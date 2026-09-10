from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
app = FastAPI()

class Image(BaseModel):
    url : HttpUrl
    name : str

class Images(BaseModel):
    Img_count : int
    Img_id : int
    Img_list : list[Image]

@app.post("/Iamges")
async def get_imgs(IMGS :Images):
    return IMGS
