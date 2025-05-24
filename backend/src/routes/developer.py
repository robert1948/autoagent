from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from backend.src.database import SessionLocal
from backend.src.models import Developer
from backend.src.schemas.developer import (
    DeveloperRegisterRequest,
    DeveloperSuccessMessage,
    DeveloperProfile
)
from backend.src.utils import hash_password
from backend.src.dependencies.auth_guard import get_current_developer

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register-developer", response_model=DeveloperSuccessMessage, status_code=status.HTTP_201_CREATED)
def register_developer(payload: DeveloperRegisterRequest, db: Session = Depends(get_db)):
    if db.query(Developer).filter(Developer.email == payload.email).first():
        raise HTTPException(
            status_code=400, detail="Developer with this email already exists"
        )

    new_dev = Developer(
        full_name=payload.fullName,
        company=payload.company,
        email=payload.email,
        portfolio=payload.portfolio,
        password=hash_password(payload.password)
    )

    db.add(new_dev)
    db.commit()
    db.refresh(new_dev)
    return {"success": True, "message": "Developer registration successful"}


@router.get("/me", response_model=DeveloperProfile)
def get_developer_profile(current_dev=Depends(get_current_developer)):
    return current_dev
