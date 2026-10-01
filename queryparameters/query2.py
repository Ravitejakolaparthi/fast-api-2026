from fastapi import FastAPI
app = FastAPI()
@app.get("/menu/{item_id}")
def home(item_id:int):
    return {
    "item_id": item_id,
    "message": "Menu item requested"
}
@app.get("/menu")
def menu(category:str) :
    if(category == "veg"):
        return {
            "category":"veg",
            "message":"Showing veg menu"
        }
    if(category == "Non Veg"):
        return {
            "category":"Non veg",
            "Messege" : "showing Non Veg items"
        }
    else :
        return None