# backend/src/routes/user.py

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

router = APIRouter()

# In-memory storage (replace with DB later)
user_db = []


class UserRegisterRequest(BaseModel):
    fullName: str
    username: str
    email: EmailStr
    password: str


@router.post("/register-user")
def register_user(data: UserRegisterRequest):
    # Check for duplicate email or username
    for user in user_db:
        if user['email'] == data.email:
            raise HTTPException(status_code=400, detail="Email already exists")
        if user['username'] == data.username:
            raise HTTPException(
                status_code=400, detail="Username already exists")

    # Store user (password should be hashed in production)
    user_db.append({
        "fullName": data.fullName,
        "username": data.username,
        "email": data.email,
        "password": data.password,
        "verified": False,
    })

    return {"success": True, "message": "User registered. Please verify your email."}
