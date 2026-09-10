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
class Studio(BaseModel):
    Studio_name : str
    Imgs : Images 

@app.post("/Iamges")
async def get_imgs(std : Studio):
    return std