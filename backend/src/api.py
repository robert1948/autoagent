from fastapi import APIRouter
from routes.developer import router as developer_router
from routes.user import router as user_router  # 👈 Add this

router = APIRouter()

router.include_router(
    developer_router, prefix="/developer", tags=["Developer"])
router.include_router(user_router, prefix="/user",
                      tags=["User"])  # 👈 Register user routes
