import uvicorn
from fastapi import FastAPI

from users.views import router as users_router

app = FastAPI()
app.include_router(users_router)


@app.get('/')
def read_root():
    return {'message': 'Hello, Index!'}


@app.get('/hello/')
def read_name_and_print_hello(name: str):
    name = name.strip().title()
    return {'message': f'Hello, {name}'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
