from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
app = FastAPI()
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
Tables = [
      {
            "id":1,
            "table_number":1,
            "capacity": 2
      },
      {
            "id":2,
            "table_number":2,
            "capacity":4
      },
      {
            "id":3,
            "table_number":3,
            "capacity":6
      }
]

@app.post("/tables",response_model=TableOut)
def Create_table(table:Table):
      id = len(Tables)+1
      data = table.model_dump()
      data["id"] = id
      Tables.append(data)
      return data

@app.get("/tables",response_model=list[TableOut])
def Show_all_tables():
      return Tables

@app.get("/tables/{table_id}",response_model=TableOut)
def show_table(table_id:int):
      for table in Tables :
        if table["id"] == table_id :
            return table
      raise HTTPException(
           status_code=404,
           detail="Not Found"
      )
@app.patch("/tables/{table_id}",response_model=TableOut)
def Update_table(table_id:int,UpdatingTable:TableUpdate):
     for table in Tables:
        if table["id"] == table_id:
           data = UpdatingTable.model_dump(exclude_unset=True)
           table.update(data)
           return table

     raise HTTPException(
          status_code=404,
          detail="Not Found"
     )
@app.delete("/tables/{table_id}")
def delete_table(table_id:int):
     for key, table in enumerate(Tables) :
          if table["id"] == table_id:
                Tables.pop(key)
                return {
                     "messege":"Data Deleted SuccessFully"
                }
     raise HTTPException(
          status_code=404,
          detail="Not Found"
     )
