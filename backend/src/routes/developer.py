from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, HttpUrl

router = APIRouter()

# In-memory storage for now
developer_db = []


class DeveloperRequest(BaseModel):
    fullName: str
    company: str
    email: EmailStr
    portfolio: HttpUrl
    password: str


@router.post("/register-developer")
def register_developer(data: DeveloperRequest):
    for dev in developer_db:
        if dev['email'] == data.email:
            raise HTTPException(status_code=400, detail="Email already exists")

    developer_db.append({
        "fullName": data.fullName,
        "company": data.company,
        "email": data.email,
        "portfolio": str(data.portfolio),
        "password": data.password,
        "status": "pending"
    })

    return {"success": True, "message": "Developer application submitted"}
