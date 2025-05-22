from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from backend.src.database import SessionLocal
from backend.src.models import User
import os

# OAuth2 scheme (expects Authorization: Bearer <token>)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

# Get secret and algorithm from environment or fallback
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")  # Set in Heroku config
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# DB Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get current user based on token


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if not email:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise credentials_exception

    return user
