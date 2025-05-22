from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from backend.src.utils import hash_password, verify_password
from backend.src.database import SessionLocal
from backend.src.models import User
from backend.src.auth import create_access_token
from backend.src.dependencies.auth_guard import get_current_user  # ✅ Auth dependency

router = APIRouter()

# ----- DB Dependency -----


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----- REGISTER -----


class UserRegisterRequest(BaseModel):
    fullName: str
    username: str
    email: EmailStr
    password: str


@router.post("/register-user")
def register_user(data: UserRegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        (User.email == data.email) | (User.username == data.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already exists"
        )

    hashed_pw = hash_password(data.password)

    new_user = User(
        full_name=data.fullName,
        username=data.username,
        email=data.email,
        password=hashed_pw,
        verified=False,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"success": True, "message": "User registered. Please verify your email."}

# ----- LOGIN -----


class LoginRequest(BaseModel):
    identifier: str  # email or username
    password: str


@router.post("/login")
def login_user(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        (User.email == data.identifier) | (User.username == data.identifier)
    ).first()

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email/username or password"
        )

    token = create_access_token({"sub": user.email})

    return {
        "success": True,
        "token": token,
        "message": f"Welcome back, {user.full_name}!"
    }

# ----- PROFILE (/me) -----


@router.get("/me")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "fullName": current_user.full_name,
        "username": current_user.username,
        "email": current_user.email,
        "verified": current_user.verified
    }
