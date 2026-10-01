from fastapi import FastAPI
app = FastAPI()
@app.post("/menu")
def add_menu(data:dict):
    return data
