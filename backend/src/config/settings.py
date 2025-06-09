# filepath: /workspaces/autoagent/backend/src/config/settings.py

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    FRONTEND_ORIGIN: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
print("🔍 Loaded DATABASE_URL from environment:", settings.DATABASE_URL)
