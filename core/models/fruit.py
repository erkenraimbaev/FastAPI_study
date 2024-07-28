from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Fruit(Base):
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    price: Mapped[str]
