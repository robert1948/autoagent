# backend/src/main.py

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from backend.src.routes import router as api_router
from backend.src.database import engine
from backend.src.models import Base

# --- Load environment variables ---
load_dotenv()

# --- Validate critical env vars ---
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("❌ DATABASE_URL not set in .env")
if not os.getenv("SECRET_KEY"):
    raise RuntimeError("❌ SECRET_KEY not set in .env")

# --- FastAPI App Initialization ---
app = FastAPI(
    title="AutoAgent API",
    version="1.0.0",
    description="Backend for AutoAgent with user and developer registration",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# --- CORS Configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔐 Consider restricting in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Database Initialization ---


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


# --- Register API Routers ---
app.include_router(api_router, prefix="/api")

# --- Health Check Endpoint ---


@app.get("/")
def read_root():
    return {"message": "AutoAgent backend is running"}

# --- Custom Swagger UI with Dev JWT Hint ---


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    dev_token = os.getenv("DEV_JWT", "Bearer YOUR_DEV_JWT_HERE")

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": f"Paste the token below:\n\n`{dev_token}`"
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
