import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get('/')
def read_root():
    return {'message': 'Hello, Index!'}


@app.get('/hello/')
def read_name_and_print_hello(name: str):
    name = name.strip().title()
    return {'message': f'Hello, {name}'}


@app.post('/users/create/')
def create_user(user: CreateUser):
    return {'message': 'User was created',
            'email': user.email
            }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
