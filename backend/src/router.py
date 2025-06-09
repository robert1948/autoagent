from fastapi import APIRouter

# Available routers
from routes.developer import router as developer_router
# from routes.api.auth import router as auth_router  # Auth module not found
# from routes.api.dashboard import router as dashboard_router  # Dashboard not found
from routes.onboarding import router as onboarding_router

router = APIRouter()

# Register sub-routers
router.include_router(
    developer_router, prefix="/developers", tags=["developers"])
# router.include_router(auth_router, prefix="/auth", tags=["auth"])  # Auth commented out
router.include_router(
    onboarding_router, prefix="/onboarding", tags=["onboarding"])
# router.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])  # Dashboard commented out

# Note: The commented-out routes are placeholders for future implementation.
