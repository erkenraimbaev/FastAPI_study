from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from schemas.fruit import Fruit, FruitCreate


async def get_fruits(session: AsyncSession) -> list[Fruit]:
    stat = select(Fruit).order_by(Fruit.id)
    result: Result = await session.execute(stat)
    fruits = result.scalars().all()
    return list(fruits)


async def get_fruit(session: AsyncSession) -> Fruit | None:
    return await session.get(Fruit, Fruit.id)


async def create_fruit(session: AsyncSession, fruit_in: FruitCreate) -> Fruit:
    fruit = Fruit(**fruit_in.model_dump())
    session.add(fruit)
    await session.commit()
    # await session.refresh()
    return fruit




