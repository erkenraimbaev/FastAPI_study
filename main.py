from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello, world!'}


@app.get('/hello/{name}')
def read_name_and_print_hello(name: str):
    return {'message': f'Hello, {name}'}
