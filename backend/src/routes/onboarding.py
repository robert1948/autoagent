# filepath: backend/src/router/onboarding.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Developer
from schemas.developer import OnboardingUpdateRequest, OnboardingState
from dependencies.auth_guard import get_current_developer

router = APIRouter()

# Dependency to provide DB session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=OnboardingState)
def get_onboarding_status(current_developer: Developer = Depends(get_current_developer)):
    if not current_developer.onboarding:
        raise HTTPException(
            status_code=404, detail="Onboarding data not found.")
    return current_developer.onboarding


@router.patch("/", response_model=dict)
def update_onboarding(
    payload: OnboardingUpdateRequest,
    current_developer: Developer = Depends(get_current_developer),
    db: Session = Depends(get_db)
):
    current_developer.onboarding = payload.onboarding
    db.commit()
    return {"success": True, "message": "Onboarding status updated"}
