from fastapi import FastAPI
app = FastAPI()
@app.get('/item/{item}')
async def read_item(item :int):
    return {"item ":item}
