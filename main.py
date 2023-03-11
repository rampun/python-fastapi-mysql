from fastapi import FastAPI, APIRouter
from routes.index import user
from config.db import meta, engine

app = FastAPI()

meta.create_all(engine)

app.include_router(user)
