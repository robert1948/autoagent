from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from src.config.settings import settings
from src.database import engine
from src.models import Base
from src.router import router as api_router

app = FastAPI(
    title="AutoAgent API",
    description="API for user and developer registration, login, and profile management",
    version="1.0.0"
)

# Create tables
Base.metadata.create_all(bind=engine)

# CORS for development/testing (adjust as needed for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static React files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve favicon


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("static/favicon.ico")

# Serve React frontend index.html


@app.get("/", include_in_schema=False)
def serve_frontend():
    index_path = "static/index.html"
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "AutoAgent backend is running"}


# Include API routes
app.include_router(api_router)
