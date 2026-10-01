from fastapi import FastAPI
app = FastAPI()
menu_items = {
    "veg" : ["Paneer","BagaraRice","Gobi Manchurian"],
    "non veg":["Chinken curry","BagaraRice","Chinken Manchurian"],
    "drinks":["Pepsi","CocoCola","ThumsUp"]
}
@app.get("/menu")
def get_menu(category:str):
    if(category == "all"):
        return menu_items
    else:
        return {
            "category" : category,
            "items" : menu_items[category]
        }