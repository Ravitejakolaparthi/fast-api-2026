from fastapi import FastAPI
app = FastAPI()
@app.get("/path/{num}")
async def get_num(num:int):
    return num

