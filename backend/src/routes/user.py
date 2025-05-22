from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from backend.src.utils import hash_password
from backend.src.database import SessionLocal
from backend.src.models import User

router = APIRouter()

# Dependency to get a DB session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserRegisterRequest(BaseModel):
    fullName: str
    username: str
    email: EmailStr
    password: str


@router.post("/register-user")
def register_user(data: UserRegisterRequest, db: Session = Depends(get_db)):
    # Check for duplicate email or username
    existing_user = db.query(User).filter(
        (User.email == data.email) | (User.username == data.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already exists"
        )

    # Hash the password
    hashed_pw = hash_password(data.password)

    # Create and store user
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
