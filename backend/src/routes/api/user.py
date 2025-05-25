from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from src.utils import hash_password, verify_password
from src.database import SessionLocal
from src.models import User
from src.auth import create_access_token
from src.dependencies.auth_guard import get_current_user
from src.schemas.user import UserRegisterRequest, UserProfile, LoginRequest, SuccessMessage

router = APIRouter()

# ----- DB Dependency -----


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----- REGISTER -----


@router.post("/register-user", response_model=SuccessMessage, status_code=status.HTTP_201_CREATED)
def register_user(data: UserRegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new user with hashed password and email/username uniqueness check.
    """
    existing_user = db.query(User).filter(
        (User.email == data.email) | (User.username == data.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already exists"
        )

    new_user = User(
        full_name=data.full_name,
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password),
        verified=False,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return SuccessMessage(message="User registered. Please verify your email.")

# ----- LOGIN -----


@router.post("/login")
def login_user(data: LoginRequest, db: Session = Depends(get_db)):
    """
    Authenticate user using email or username and return JWT token.
    """
    user = db.query(User).filter(
        (User.email == data.identifier) | (User.username == data.identifier)
    ).first()

    if not user or not verify_password(data.password, user.hashed_password):
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


@router.get("/me", response_model=UserProfile)
def get_profile(current_user: User = Depends(get_current_user)):
    """
    Retrieve authenticated user's profile.
    """
    return UserProfile(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username,
        email=current_user.email,
        role=current_user.role,
        verified=current_user.verified
    )

# ----- DEBUG USERS -----


@router.get("/debug/users")
def debug_users(db: Session = Depends(get_db)):
    """
    ⚠️ TEMPORARY DEBUG ENDPOINT
    Lists all users in the database.
    REMOVE after debugging to prevent sensitive data exposure.
    """
    users = db.query(User).all()
    return [
        {
            "id": user.id,
            "full_name": user.full_name,
            "username": user.username,
            "email": user.email,
            "verified": user.verified
        }
        for user in users
    ]
