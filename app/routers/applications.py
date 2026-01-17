from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..db import get_db
from .. import models, schemas

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("", response_model=schemas.ApplicationOut)
def create_application(payload: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    app = models.Application(
        company=payload.company.strip(),
        role=payload.role.strip(),
        link=(payload.link.strip() if payload.link else None),
        status=payload.status.strip(),
        notes=payload.notes,
    )
    db.add(app)
    db.commit()
    db.refresh(app)
    return app


@router.get("", response_model=List[schemas.ApplicationOut])
def list_applications(db: Session = Depends(get_db)):
    return db.query(models.Application).order_by(models.Application.created_at.desc()).all()
