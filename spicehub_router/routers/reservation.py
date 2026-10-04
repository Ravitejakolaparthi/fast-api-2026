from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,Field
router = APIRouter(
    prefix="/reservations"
)
Reservations = [
    {
        "id": 1,
        "customer_id": 1,
        "table_number": 2,
        "guests": 3
    }
]

class reservationIn(BaseModel):
    customer_id : int
    table_number : int = Field(gt = 0)
    guests : int = Field(gt = 0)

class reservationOut(BaseModel):
    id : int
    customer_id : int
    table_number : int 
    guests : int =Field(gt = 0)
class reservationUpdate(BaseModel):
    id : int | None = Field(gt= 0)
    customer_id : int | None =Field(gt= 0)
    table_number : int | None= Field(gt= 0)
    guests : int | None = Field(gt= 0)

@router.get("",response_model=list[reservationOut])
def get_reservations():
    return Reservations

@router.get("/{reservation_id}",response_model=reservationOut)
def get_reservation(reservation_id:int):
    for reservation in Reservations :
        if reservation["id"] == reservation_id:
            return reservation
    raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
@router.post("",response_model=reservationOut)
def Create_reservation(reservation : reservationIn):
    new_reservation = reservation.model_dump()
    new_reservation["id"] = len(Reservations)+1
    Reservations.append(new_reservation)
    return new_reservation
@router.patch("/{reservation_id}",response_model=reservationOut)
def Update_reservation(reservation_id : int,reservation:reservationUpdate):
    Updated_reservation = reservation.model_dump(exclude_unset=True)
    for reservations in Reservations :
        if reservations["id"] == reservation_id :
            reservations.update(Updated_reservation)
            return reservation
    raise HTTPException(
        status_code=404,
        detail="Not Found"
    )
@router.delete("/{reservation_id}",response_model=reservationOut)
def delete_reservation(reservation_id:int):
    for index ,reservation in enumerate(Reservations):
        if reservation["id"] == reservation_id :
            return Reservations.pop(index)
    raise HTTPException(
            status_code=404,
            detail="Not Found"
        )
