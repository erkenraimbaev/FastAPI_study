from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    username: str
    first_name: str
    email: EmailStr


class UserCreate(BaseModel):
    username: str
    first_name: str
    email: EmailStr
