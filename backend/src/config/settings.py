from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    FRONTEND_ORIGIN: str  # ✅ Required for CORS

    class Config:
        env_file = ".env"


# ✅ This must be at the bottom
settings = Settings()
