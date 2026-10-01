from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,Field
router = APIRouter(
    prefix="/customers"
)

Customers = [
    {"id": 1, "name": "Ravi", "active": True},
    {"id": 2, "name": "Teja", "active": True},
    {"id": 3, "name": "Sai", "active": False},
]

class CustomersIn(BaseModel):
    name : str
    active : bool 

class CustomersOut(BaseModel):
    id : int
    name : str


@router.get("",response_model=list[CustomersOut])
def get_Customers():
    return Customers

@router.get("/{customer_id}",response_model=CustomersOut)
def get_customer(customer_id : int):
    for customer in Customers:
        if customer["id"] == customer_id :
            return customer

@router.post("")
def create_customer(customer : CustomersIn):
    customer_id = len(Customers)+1
    new_customer = customer.model_dump()
    new_customer["id"] = customer_id
    Customers.append(new_customer)
    return new_customer




