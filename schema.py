# build a schema using pydantic
from datetime import date
from pydantic import BaseModel


class Club(BaseModel):
    name: str
    description: str
    address: str

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    birth: date

    class Config:
        orm_mode = True
