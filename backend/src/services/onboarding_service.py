# backend/src/services/onboarding_service.py

from sqlalchemy.orm import Session
from backend.src.models import Developer
from backend.src.schemas.developer import OnboardingState


async def get_onboarding_status(db: Session, developer_id: int) -> OnboardingState:
    """
    Retrieve onboarding status for a developer.
    """
    developer = db.query(Developer).filter(
        Developer.id == developer_id).first()
    if developer is None:
        raise Exception("Developer not found.")

    # If onboarding is None, return an empty state
    if developer.onboarding is None:
        return OnboardingState(steps=[], completed=False)

    # Convert stored dict to Pydantic schema
    return OnboardingState(**developer.onboarding)


async def update_onboarding(db: Session, developer_id: int, onboarding_data: OnboardingState):
    """
    Update onboarding data for a developer.
    """
    developer = db.query(Developer).filter(
        Developer.id == developer_id).first()
    if developer is None:
        raise Exception("Developer not found.")

    developer.onboarding = onboarding_data.dict()  # Save as JSON/dict
    db.commit()
    return {"success": True, "message": "Onboarding updated"}
