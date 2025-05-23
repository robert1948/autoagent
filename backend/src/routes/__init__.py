# backend/src/routes/__init__.py
from fastapi import APIRouter
from backend.src.routes.developer import router as developer_router
from backend.src.routes.user import router as user_router

router = APIRouter()
router.include_router(
    developer_router, prefix="/developer", tags=["Developer"])
router.include_router(user_router, prefix="/user", tags=["User"])
