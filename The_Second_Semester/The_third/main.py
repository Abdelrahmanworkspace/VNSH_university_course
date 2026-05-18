import os
from contextlib import asynccontextmanager
from typing import Annotated

import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, StringConstraints
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from models import Base, UserModel


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL)
session_maker = async_sessionmaker(engine, expire_on_commit=False)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


class UserCreateSchema(BaseModel):
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
    login: Annotated[str, StringConstraints(min_length=3, max_length=20)]
    password: Annotated[str, StringConstraints(min_length=6)]


class UserSchema(BaseModel):
    id: int
    name: str
    login: str


@app.post("/users/register")
async def register(body: UserCreateSchema) -> UserSchema:
    async with session_maker() as session:
        existing_user = await session.execute(
            select(UserModel).where(UserModel.login == body.login)
        )
        if existing_user.scalar_one_or_none() is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="this login already exists"
            )

        new_user = UserModel(
            name=body.name,
            login=body.login,
            password=body.password,
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

    return new_user


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
