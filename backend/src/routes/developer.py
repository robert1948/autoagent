from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database import SessionLocal
from src.models import Developer
from src.schemas.developer import (
    DeveloperRegisterRequest,
    DeveloperProfile,
)
from src.schemas.user import SuccessMessage  # ✅ Shared schema
from src.utils import hash_password
from src.dependencies.auth_guard import get_current_developer

router = APIRouter()


# Dependency to provide DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register-developer", response_model=SuccessMessage, status_code=status.HTTP_201_CREATED)
def register_developer(data: DeveloperRegisterRequest, db: Session = Depends(get_db)):
    if db.query(Developer).filter_by(email=data.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Developer with this email already exists"
        )

    developer = Developer(
        full_name=data.full_name,
        email=data.email,
        hashed_password=hash_password(data.password),
    )
    db.add(developer)
    db.commit()
    db.refresh(developer)
    return SuccessMessage(message="Developer registered successfully")


@router.get("/developer/me", response_model=DeveloperProfile)
def get_developer_profile(current_developer: Developer = Depends(get_current_developer)):
    return current_developer
