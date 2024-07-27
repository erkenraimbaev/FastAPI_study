from typing import Annotated

from fastapi import APIRouter, Path

from users.schemas import CreateUser

from users import crud

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/create/')
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)


@router.get('/{user_id}')
def get_user(user_id: Annotated[int, Path(ge=1, le=1000000)]):
    return f'User has id: {user_id}'
