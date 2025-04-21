from datetime import datetime, date
from typing import Optional, Any, Annotated

from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError, BeforeValidator, AfterValidator
from pydantic_core.core_schema import computed_field


def validate_id(id_):
    return id_


class Order(BaseModel):
    ...

class User(BaseModel):
    id: int = Annotated[int, AfterValidator(validate_id)]
    name: str | None = Field(min_length=3, max_length=20)
    # name: Optional[str]
    # age: int = 0
    # age: int = Field(default=30, gt=0, le=200)
    birth_date : date | None = None
    email: EmailStr
    items: list[int] = Field(default_factory=list)
    orders: dict[str, Order] | None = None


    @field_validator("name", mode="before")
    @classmethod
    def name_validator(cls, value):
        if isinstance(value, str):
            return value
        elif isinstance(value, list):
            return " ".join(value)
        else:
            raise ValidationError("name", "must be list or str")

    # @computed_field
    # def age(self) -> int:
    #     return int((date.today() - self.birth_date).days / 365)


class SuperUser(User):
    is_admin: bool = True

# class Square(BaseModel):
#     width: float
#
#     @computed_field
#     def area(self) -> float:  # converted to a `property` by `computed_field`
#         return round(self.width**2, 2)


# s = Square(width=2)

u = User(id=1, name = ["first", "last"], age="100", email="email@hcbdjcds.com")
print(u)
# print({}.get("nama", "Default"))
# print(u.nama)

user_dumped = u.model_dump()
user_json = u.model_dump_json()



print(type(user_dumped))
print(user_dumped)


print(type(user_json))
print(user_json)


user_from_foreign = User.model_validate_json(user_json)
print(type(user_from_foreign))
print(user_from_foreign)
print(user_from_foreign.items)

# def func(i, arg1: list = None):
#     if arg1 is None:
#         arg1 = list()
#     arg1.append(i)
#     print(arg1)
#
#
# func(1)
# func(2)