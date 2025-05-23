from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from backend.src.routes import router as api_router  # ✅ Correct import
from backend.src.database import engine
from backend.src.models import Base
import os

app = FastAPI(
    title="AutoAgent API",
    version="1.0.0",
    description="Backend for AutoAgent with user and developer registration",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# --- CORS CONFIG ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔐 Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CREATE DB TABLES ON STARTUP ---


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


# --- ROUTES ---
app.include_router(api_router, prefix="/api")

# --- HEALTH CHECK ---


@app.get("/")
def read_root():
    return {"message": "AutoAgent backend is running"}

# --- SWAGGER OPENAPI CONFIG WITH DEV JWT ---


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
