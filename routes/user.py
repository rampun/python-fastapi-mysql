from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
from sqlalchemy.sql import text
from sqlalchemy import select, update, insert, delete

user = APIRouter()


@user.get('/')
async def read_data():
    stmt = select(users)
    return conn.execute(stmt).mappings().all()


@user.get('/{id}')
async def read_single_data(id: int):
    stmt = select(users).where(users.c.id == id)
    return conn.execute(stmt).mappings().all()


@user.post('/')
async def write_data(user: User):
    stmt = insert(users).values(
        name=user.name,
        email=user.email,
        password=user.password
    )
    conn.execute(stmt)
    conn.commit()

    return conn.execute(select(users)).mappings().all()


@user.put('/{id}')
async def update_data(id: int, user: User):
    stmt = update(users).where(users.c.id == id).values(
        name=user.name,
        email=user.email,
        password=user.password
    )

    conn.execute(stmt)
    conn.commit()
    return conn.execute(select(users).where(users.c.id == id)).mappings().all()


@user.delete('/{id}')
async def delete_data(id: int):
    stmt = delete(users).where(users.c.id == id)
    conn.execute(stmt)
    conn.commit()
    return conn.execute(select(users)).mappings().all()
