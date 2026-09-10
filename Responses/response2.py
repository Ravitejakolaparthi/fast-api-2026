from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
app =FastAPI()
class UserIn(BaseModel):
    UserName : str
    Userid : str
    password : str
    Email : EmailStr
class UserOut(BaseModel):
    UserName :str
    Userid :str
    Email : EmailStr

@app.post("/Userdet",response_model=UserOut)
async def Create_User(user : UserIn):
    return user
