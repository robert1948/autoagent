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
        allow_population_by_field_name = True
        orm_mode = True


class LoginResponse(BaseModel):
    success: bool
    token: str
    message: str


class SuccessMessage(BaseModel):
    success: bool
    message: str
