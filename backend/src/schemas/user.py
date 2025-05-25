from pydantic import BaseModel, EmailStr


class UserRegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserProfile(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str


class SuccessMessage(BaseModel):
    message: str
