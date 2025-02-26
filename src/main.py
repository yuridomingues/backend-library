from fastapi import FastAPI
from src.models import create_tables
from src.library.router import router

def create_app():
    create_tables()

    app = FastAPI()
    app.include_router(router)
    return app

app = create_app()
