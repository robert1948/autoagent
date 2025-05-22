from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Route and DB imports
from backend.src.api import router as api_router
from backend.src.database import engine
from backend.src.models import Base

app = FastAPI(
    title="AutoAgent API",
    version="1.0.0",
    description="Backend for AutoAgent with user and developer registration"
)

# Enable CORS for dev (lock down in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Automatically create tables on startup


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


# Include API routes
app.include_router(api_router, prefix="/api")

# Health check


@app.get("/")
def read_root():
    return {"message": "AutoAgent backend is running"}
