from fastapi import FastAPI
from .db import Base, engine
from . import models  # noqa: F401 (ensures models are registered)
from .routers import applications

app = FastAPI(title="AI Job Application Assistant")

Base.metadata.create_all(bind=engine)

app.include_router(applications.router)


@app.get("/health")
def health():
    return {"status": "ok"}
