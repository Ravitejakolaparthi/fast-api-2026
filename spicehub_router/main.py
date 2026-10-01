from fastapi import FastAPI
from customers import router
app = FastAPI()
app.include_router(router)