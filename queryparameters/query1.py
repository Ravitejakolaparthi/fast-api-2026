from fastapi import FastAPI
app = FastAPI()
@app.get("/query")
async def get_query(query1 :int = 0,query2:int = 0):
    return query1,query2
