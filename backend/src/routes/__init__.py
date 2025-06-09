from fastapi import APIRouter

# Updated absolute imports without 'src.'
from routes.developer import router as developer_router
from routes.user import router as user_router

router = APIRouter()

# Mount developer and user routes to /api prefix
router.include_router(developer_router)
router.include_router(user_router)
