from fastapi import APIRouter

router = APIRouter()

# Add your endpoints here


@router.get("/users")
def get_users():
    return {"message": "User route is working"}
