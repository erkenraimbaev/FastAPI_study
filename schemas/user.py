from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import EmailStr, BaseModel, Field


class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(15)]
    first_name: str = Field(..., max_length=15)
    email: EmailStr
