from pydantic import BaseModel, EmailStr
from typing import Optional, Dict


class DeveloperLoginRequest(BaseModel):
    email: EmailStr
    password: str


class DeveloperRegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    company: Optional[str] = None
    portfolio: Optional[str] = None


class OnboardingUpdateRequest(BaseModel):
    onboarding: Dict[str, bool]


class OnboardingState(BaseModel):
    upload_portfolio: bool 
    complete_profile: bool 
    connect_github: bool 
    start_agent_task: bool 


class DeveloperProfile(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str
    company: Optional[str] = None
    portfolio: Optional[str] = None
    onboarding: Optional[Dict[str, bool]] = None

    class Config:
        from_attributes = True  # Updated for Pydantic V2
