from typing import Annotated

from fastapi import APIRouter, Path
from sqlalchemy.sql import crud

from schemas.fruit import FruitCreate


router = APIRouter(prefix='/fruits', tags=['fruits'])


@router.post('/create/')
def create_user(user: FruitCreate):
    return crud.create_user(user_in=user)


@router.get('/{user_id}')
def get_user(user_id: Annotated[int, Path(ge=1, le=1000000)]):
    return f'User has id: {user_id}'
