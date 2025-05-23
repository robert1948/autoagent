from pydantic import BaseModel, EmailStr, Field


class DeveloperRegisterRequest(BaseModel):
    fullName: str
    company: str
    email: EmailStr
    portfolio: str
    password: str


class DeveloperLoginRequest(BaseModel):
    identifier: str
    password: str


class DeveloperProfile(BaseModel):
    fullName: str = Field(..., alias="full_name")
    company: str
    email: EmailStr
    portfolio: str
    verified: bool

    class Config:
        allow_population_by_field_name = True
        orm_mode = True


class DeveloperLoginResponse(BaseModel):
    success: bool
    token: str
    message: str


class DeveloperSuccessMessage(BaseModel):
    success: bool
    message: str
