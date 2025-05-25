from pydantic import BaseModel, EmailStr


class DeveloperRegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class DeveloperProfile(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str
