from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from config.settings import settings
from router import router as api_router

app = FastAPI()

# === CORS settings ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Register backend API routes ===
app.include_router(api_router)

# === Serve React build as static files ===
static_dir = Path(__file__).parent.parent / "static"
app.mount("/static", StaticFiles(directory=static_dir / "static"), name="static")

# === Fallback route: Serve index.html for client-side routing (React SPA) ===


@app.get("/{full_path:path}", response_class=HTMLResponse)
async def serve_react_app(request: Request, full_path: str):
    index_file = static_dir / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return HTMLResponse(status_code=404, content="React frontend not found.")

# === TEST route: Display environment variables (safe for dev only) ===


@app.get("/env-check")
async def env_check():
    env_data = {
        "DATABASE_URL": settings.DATABASE_URL,
        "FRONTEND_ORIGIN": settings.FRONTEND_ORIGIN,
        "ACCESS_TOKEN_EXPIRE_MINUTES": settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        "ALGORITHM": settings.ALGORITHM,
        # Do not expose SECRET_KEY or other sensitive values here.
    }
    return JSONResponse(content=env_data)
