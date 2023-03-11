from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError

meta = MetaData()

engine = create_engine("mysql+pymysql://root:root@localhost/fastapi_test")

conn = engine.connect()
