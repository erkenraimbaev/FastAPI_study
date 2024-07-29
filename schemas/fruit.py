from pydantic import BaseModel


class FruitBase(BaseModel):
    name: str
    description: str
    price: int


class FruitCreate(FruitBase):
    pass


class Fruit(FruitBase):
    id: int

