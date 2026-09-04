from pydantic import BaseModel
class User(BaseModel):
    id : int
    name : str = "jhon doe"
    age : int
    Team_mem_id : list[int] = []

external_data = {
    "id" : "123",
    "age" : "19",
    "Team_mem_id" : [121,122,124]
}

user = User(**external_data)
print(user)
print(type(user.Team_mem_id))