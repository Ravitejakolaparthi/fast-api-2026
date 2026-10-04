from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,Field
from database import cursor,connection
router = APIRouter(
    prefix="/customers"
)

# Customers = [
#     {"id": 1, "name": "Ravi", "active": True},
#     {"id": 2, "name": "Teja", "active": True},
#     {"id": 3, "name": "Sai", "active": False},
# ]

class CustomersIn(BaseModel):
    name : str
    active : bool 

class CustomersOut(BaseModel):
    id : int
    name : str
class CustomersUpdate(BaseModel):
    id : int | None = None
    name : str | None = None


@router.get("",response_model=list[CustomersOut])
def get_Customers():
    cursor.execute("select  * from customers")
    customers = cursor.fetchall()
    result = []
    for customer in customers :
        new_customer = {
            "id" : customer[0],
            "name": customer[1],
            "active":bool(customer[2])
            }
        result.append(new_customer)
    return result

@router.get("/{customer_id}",response_model=CustomersOut)
def get_customer(customer_id : int):
    cursor.execute("select *from customers where id = ?",
                   (customer_id,))
    customer = cursor.fetchone()
    if customer is None :
         raise HTTPException(
                status_code=404,
                detail="Customer Not Found"
            )
    the_customer = {
        "id" : customer[0],
        "name":customer[1],
        "active":bool(customer[2])
           }
    return the_customer
   

@router.post("")
def create_customer(customer : CustomersIn):
    new_customer = customer.model_dump()
    cursor.execute("insert into customers (name,active) values (?,?)",(customer.name,customer.active))
    connection.commit()
    customer_id = cursor.lastrowid
    new_customer["id"] = customer_id
    return new_customer

@router.patch("/{customer_id}",response_model=CustomersOut)
def Update_customer(customer_id : int,customer : CustomersUpdate):
    Updating_customer = customer.model_dump(exclude_unset=True)
    set_parts = []
    for key in Updating_customer :
        set_parts.append(f"{key} = ?")
    set_clause = ",".join(set_parts)
    values = list(Updating_customer.values()) + [customer_id]

    cursor.execute(f"update customers set {set_clause} where id = ?",values)
    connection.commit()
    cursor.execute("select * from customers where id = ?",(customer_id,))
    updated_customer = cursor.fetchone()
    if updated_customer is None :
        raise HTTPException(
           status_code=400,
           detail="Customer Not Found" 
        )
    return {
        "id" : updated_customer[0],
        "name":updated_customer[1],
        "active":bool(updated_customer[2])
    }