from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from backend.src.database import SessionLocal
from backend.src.models import Developer
from backend.src.utils import hash_password, verify_password
from backend.src.auth import create_access_token
from backend.src.schemas.developer import DeveloperRegisterRequest, DeveloperProfile

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DeveloperRequest(BaseModel):
    fullName: str
    company: str
    email: EmailStr
    portfolio: str
    password: str


class DeveloperLoginRequest(BaseModel):
    identifier: str
    password: str


class LoginResponse(BaseModel):
    success: bool
    token: str
    message: str


class SuccessMessage(BaseModel):
    success: bool
    message: str


@router.post("/register-developer", response_model=SuccessMessage)
def register_developer(data: DeveloperRequest, db: Session = Depends(get_db)):
    existing = db.query(Developer).filter(
        Developer.email == data.email).first()
    if existing:
        raise HTTPException(
            status_code=400, detail="Developer already registered")

    new_dev = Developer(
        full_name=data.fullName,
        company=data.company,
        email=data.email,
        portfolio=data.portfolio,
        password=hash_password(data.password)
    )
    db.add(new_dev)
    db.commit()
    db.refresh(new_dev)

    return {"success": True, "message": "Developer registration submitted"}


@router.post("/login", response_model=LoginResponse)
def login_developer(data: DeveloperLoginRequest, db: Session = Depends(get_db)):
    dev = db.query(Developer).filter(
        Developer.email == data.identifier).first()
    if not dev or not verify_password(data.password, dev.password):
        raise HTTPException(status_code=401, detail="Invalid login")

    token = create_access_token({"sub": dev.email})
    return {
        "success": True,
        "token": token,
        "message": f"Welcome back, {dev.full_name}!"
    }
