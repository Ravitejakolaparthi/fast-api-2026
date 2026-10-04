from fastapi import APIRouter,HTTPException
from pydantic import BaseModel,Field
from database import cursor,connection
router = APIRouter()
class Table(BaseModel):
    table_number : int
    capacity : int = Field(gt= 0)
    location : str | None = None
class TableOut(BaseModel):
        id : int
        table_number:int
        capacity : int
        # location : str 
class TableUpdate(BaseModel):
    #   id : int | None = None
      table_number : int | None = None
      capacity : int | None = Field(default=None,gt=0)
      location : str | None = None
# Tables = [
#       {
#             "id":1,
#             "table_number":1,
#             "capacity": 2
#       },
#       {
#             "id":2,
#             "table_number":2,
#             "capacity":4
#       },
#       {
#             "id":3,
#             "table_number":3,
#             "capacity":6
#       }
# ]

@router.post("/tables",response_model=TableOut)
def Create_table(table:Table):
     new_table=table.model_dump()
     cursor.execute("insert into tables (table_number,capacity) values(?,?)",(table.table_number,table.capacity))
     connection.commit()
     table_id = cursor.lastrowid
     new_table["id"] = table_id
     return new_table 

@router.get("/tables",response_model=list[TableOut])
def Show_all_tables():
      cursor.execute("select * from tables")
      Tables = cursor.fetchall()
      result = []
      for table in Tables :
            new_table = {
                  "id" : table[0],
                  "table_number" : table[1],
                  "capacity":table[2]
            }
            result.append(new_table)
      return result


@router.get("/tables/{table_id}",response_model=TableOut)
def show_table(table_id:int):
     cursor.execute("select * from tables where id = ?",(table_id,))
     table = cursor.fetchone()
     if table is None :
           raise HTTPException(
                 status_code=404,
                 detail="Table Not Found"
           )
     Table = {
           "id":table[0],
           "table_number":table[1],
           "capacity":table[2]
     }
     return Table
@router.patch("/tables/{table_id}",response_model=TableOut)
def Update_table(table_id:int,UpdatingTable:TableUpdate):
      data = UpdatingTable.model_dump(exclude_unset=True)
      key_parts = []
      for key in data :
            key_parts.append(f"{key}=?")
      key_values = ",".join(key_parts)
      data_values = list(data.values()) + [table_id]
      cursor.execute(f"update tables set {key_values} where id = ?",data_values)
      connection.commit()
      cursor.execute("select * from tables where id = ?",(table_id,))
      updated_table = cursor.fetchone()
      if updated_table is None :
            raise HTTPException(
                  status_code=404,
                  detail="Table Not Found"
            )
      returning_table = {
            "id" : updated_table[0],
            "table_number": updated_table[1],
            "capacity":updated_table[2]
      }
      return returning_table

      
     
@router.delete("/tables/{table_id}")
def delete_table(table_id:int):
      cursor.execute("select * from tables where id = ?",(table_id,))
      deleted_table = cursor.fetchone()
      if deleted_table is None :
            raise HTTPException(
                  status_code=404,
                  detail="Not Found"
              )
      cursor.execute("delete from tables where id = ?",(table_id,))
      connection.commit()
     
      table = {
            "id":deleted_table[0],
            "table_number":deleted_table[1],
            "capacity":deleted_table[2]
      }
      return table