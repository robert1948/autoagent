from fastapi import APIRouter

router = APIRouter()

# Add your endpoints here


@router.get("/developers")
def get_developers():
    return {"message": "Developer route is working"}
