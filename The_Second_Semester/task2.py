from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import FastAPI
from pydantic import BaseModel, StringConstraints
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column



data_base = create_async_engine("sqlite+aiosqlite:///animal_store.db")
class Base(DeclarativeBase):
    pass

class The_animal(Base):
    
    __tablename__="animals"
    id : Mapped[int]=mapped_column(primary_key=True)
    name : Mapped[str]
    type : Mapped[str]


class Users(Base):

    __tablename__ = "users"
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    login : Mapped[str]
    password : Mapped[str]


@asynccontextmanager
async def lifespan(app : FastAPI):

    async with data_base.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app=FastAPI( lifespan=lifespan )


class CreatedUser( BaseModel ) :

    name : Annotated[str ,StringConstraints( min_length=2,max_length=50 )]
    login : Annotated[str, StringConstraints(min_length=3 ,max_length=20 )]
    password : Annotated[str, StringConstraints(min_length=6)]


class UserOut(BaseModel) :
    
    name : str
    login : str


@app.post("/users/register")
def register(user_d: CreatedUser):
    
    return UserOut(name=user_d.name, login=user_d.login)