# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/home")
# async def root():
#     return {"message": "Hello World"}
from fastapi import FastAPI
import app.models as models
from app.routes import router
from app.config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/Users")

