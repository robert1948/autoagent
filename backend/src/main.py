from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the central API router using full module path for Heroku compatibility
from backend.src.api import router as api_router

app = FastAPI(
    title="AutoAgent API",
    version="1.0.0",
    description="Backend for AutoAgent with user and developer registration"
)

# CORS settings — use specific origin in production
app.add_middleware(
    CORSMiddleware,
    # Replace with ["https://your-frontend.com"] in production
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routes under /api prefix
app.include_router(api_router, prefix="/api")

# Root route for health check


@app.get("/")
def read_root():
    return {"message": "AutoAgent backend is running"}
