from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

APP_DIR = Path(__file__).resolve().parent
BASE_DIR = APP_DIR.parent


class Settings(BaseSettings):
    app_name: str = "stefanrosu-ro"
    debug: bool = False
    host: str = "127.0.0.1"
    port: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def base_dir(self) -> Path:
        return BASE_DIR

    @property
    def templates_dir(self) -> Path:
        return self.base_dir / "templates"

    @property
    def static_dir(self) -> Path:
        return self.base_dir / "static"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
