from fastapi import FastAPI
import models
from database import engine
from routers import auth_v1, auth_v2, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth_v1.router)
app.include_router(auth_v2.router)
app.include_router(todos.router)
