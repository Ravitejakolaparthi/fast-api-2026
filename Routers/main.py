from fastapi import FastAPI
app = FastAPI()
from orders import router
app.include_router(router)
