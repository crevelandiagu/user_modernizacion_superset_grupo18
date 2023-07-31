from fastapi import FastAPI
from app.users.views import router
from app.config.db import start_db
# app = FastAPI()

app = FastAPI()
app.include_router(router, prefix="/user", tags=["Users Management"])
start_db()

