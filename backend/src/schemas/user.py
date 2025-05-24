# backend/src/schemas/user.py

from pydantic import BaseModel, EmailStr, Field


class UserRegisterRequest(BaseModel):
    fullName: str
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    identifier: str
    password: str


class UserProfile(BaseModel):
    fullName: str = Field(..., alias="full_name")
    username: str
    email: EmailStr
    verified: bool

    class Config:
        populate_by_name = True  # Updated for Pydantic v2
        from_attributes = True


class LoginResponse(BaseModel):
    success: bool
    token: str
    message: str


class SuccessMessage(BaseModel):
    success: bool
    message: str
