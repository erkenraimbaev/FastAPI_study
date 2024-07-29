from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from models import engine, Base
from routers.user import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)


@app.get('/')
def read_root():
    """
    Главная страница сайта
    :return:
    """
    return {'message': 'It"s Homepage! !'}


@app.get('/hello/')
def read_name_and_print_hello(name: str):
    """
    Функция с отправкой данных в query string
    :param name:
    :return:
    """
    name = name.strip().title()
    return {'message': f'Hello, {name}'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
