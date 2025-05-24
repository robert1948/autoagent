from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from backend.src.database import SessionLocal
from backend.src.models import User
from backend.src.schemas.user import UserRegisterRequest, SuccessMessage
from backend.src.utils import hash_password  # ✅ import hash utility

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register-user", response_model=SuccessMessage, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserRegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(
            status_code=400, detail="User with this email already exists"
        )

    new_user = User(
        full_name=payload.fullName,
        username=payload.username,
        email=payload.email,
        # ✅ hash the password before storing
        password=hash_password(payload.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"success": True, "message": "User registration successful"}
