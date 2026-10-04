from fastapi import FastAPI
from routers.customers import router as customer_router
# from routers.reservation import router as reservation_router
# from routers.menu import router as menu_router
from routers.tables import router as table_router
app = FastAPI()
# app.include_router(customer_router)
# app.include_router(reservation_router)
# app.include_router(menu_router)
app.include_router(table_router)
