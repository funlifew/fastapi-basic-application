from fastapi import FastAPI
from app.routers import echo, health

app = FastAPI(title="Simple FastAPI Project")

app.include_router(echo.router)
app.include_router(health.router)