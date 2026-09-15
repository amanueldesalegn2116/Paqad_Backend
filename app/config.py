from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "sqlite:///./paqad.db"
    allowed_origins: str = "http://localhost:3000,http://localhost:8081"
    app_env: str = "development"
    app_secret_key: str = "change-me-in-production"
    nvidia_api_key: str = ""


@lru_cache()
def get_settings() -> Settings:
    return Settings()
