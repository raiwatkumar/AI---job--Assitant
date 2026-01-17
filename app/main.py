from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine
from . import models  # noqa: F401 (ensures models are registered)
from .routers import applications
import os

app = FastAPI(title="AI Job Application Assistant")

# Create tables (for dev; consider Alembic for prod)
Base.metadata.create_all(bind=engine)

# CORS setup
origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(applications.router)


@app.get("/health")
def health():
    return {"status": "ok"}
