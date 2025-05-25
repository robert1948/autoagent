from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from src.config.settings import settings
from src.database import engine
from src.models import Base
from src.router import router as api_router

app = FastAPI(
    title="AutoAgent API",
    description="API for user and developer registration, login, and profile management",
    version="1.0.0"
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],  # e.g. http://localhost:3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (e.g., favicon.ico)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve favicon at /favicon.ico


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse("static/favicon.ico")

# Welcome route


@app.get("/", response_class=HTMLResponse)
def root():
    return "<h2>🚀 AutoAgent API is running.</h2><p>Visit <a href='/docs'>/docs</a> to explore the API.</p>"


# Mount your API router
app.include_router(api_router)
