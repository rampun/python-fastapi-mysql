from config.db import engine, meta
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String


users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('password', String(255))
)
