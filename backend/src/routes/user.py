from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from backend.src.utils import hash_password  # ✅ import the utility

router = APIRouter()

user_db = []  # Simulated DB


class UserRegisterRequest(BaseModel):
    fullName: str
    username: str
    email: EmailStr
    password: str


@router.post("/register-user")
def register_user(data: UserRegisterRequest):
    # Check if email or username already exists
    for user in user_db:
        if user['email'] == data.email:
            raise HTTPException(status_code=400, detail="Email already exists")
        if user['username'] == data.username:
            raise HTTPException(
                status_code=400, detail="Username already exists")

    # ✅ Hash the password
    hashed_pw = hash_password(data.password)

    user_db.append({
        "fullName": data.fullName,
        "username": data.username,
        "email": data.email,
        "password": hashed_pw,
        "verified": False,
    })

    return {"success": True, "message": "User registered. Please verify your email."}
