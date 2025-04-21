from pydantic import BaseModel
from dataclasses import dataclass


@dataclass
class UserDC:
    id: int
    name: str
    age: int
    email: str


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str


u = User(id=1, name = "Name", age="100 years", email="email")
print(type(u.age))
# u_dc = UserDC(id=1, name = "Name", age="100 years", email="email")
# print(type(u_dc.age))
# print(u_dc.age)

