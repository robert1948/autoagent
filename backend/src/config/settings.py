# filepath: /workspaces/autoagent/backend/src/config/settings.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    FRONTEND_ORIGIN: str

    class Config:
        # This ensures:
        # ✅ In local dev: reads .env file
        # ✅ In Heroku: uses config vars automatically
        env_file = "../../.env"   # Adjust if your .env is in root or backend
        env_file_encoding = "utf-8"


settings = Settings()
print("🔍 Loaded DATABASE_URL from environment:", settings.DATABASE_URL)
