from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer
from backend.src.api import router as api_router
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
    allow_origins=["*"],  # 🔐 Replace with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- TABLE CREATION ---
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# --- ROUTES ---
app.include_router(api_router, prefix="/api")

# --- HEALTH CHECK ---
@app.get("/")
def read_root():
    return {"message": "AutoAgent backend is running"}

# --- OAUTH2 SCHEME ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

# --- CUSTOM OPENAPI WITH DEV TOKEN ---
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    dev_token = os.getenv("DEV_JWT", "Bearer YOUR_DEV_JWT_HERE")

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": f"**Authorization header**: `Bearer <token>`\n\n**Dev Token:**\n\n`{dev_token}`"
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            if "security" not in method:
                method["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
