from fastapi import FastAPI
app = FastAPI()
@app.get("/vaild")
async def is_vaild(val : int | None= None):
    return {"item":[{"item1":"ChocoBar"},{"item2":"cocoBar"}]}
