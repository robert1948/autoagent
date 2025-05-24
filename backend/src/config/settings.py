# NEW
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    DEV_JWT: str = "Bearer YOUR_DEV_JWT_HERE"

    class Config:
        env_file = ".env"


settings = Settings()
