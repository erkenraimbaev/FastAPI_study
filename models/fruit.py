from pydantic import BaseModel


class Fruit(BaseModel):
    id: int
    name: str
    description: str
    price: int


class FruitCreate(BaseModel):
    name: str
    description: str
    price: int

