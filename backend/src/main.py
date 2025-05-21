# backend/src/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# assuming all routes (including developer) are included there
from api import router as api_router

app = FastAPI()

# Enable CORS for frontend development (adjust origin in production)
app.add_middleware(
    CORSMiddleware,
    # Replace with ["http://localhost:3000"] in production
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount all API routes under /api
app.include_router(api_router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "AutoAgent backend is running"}
