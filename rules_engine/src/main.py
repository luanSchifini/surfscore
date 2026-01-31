from fastapi import FastAPI
from fastapi import FastAPI
from rules_engine.src.api.router import api_router

app = FastAPI(
    title="Surf Score Rules Engine",
    version="1.0.0"
)

app.include_router(api_router)
