from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

APP_DIR = Path(__file__).resolve().parent
BASE_DIR = APP_DIR.parent


class Settings(BaseSettings):
    app_name: str = "stefanrosu-ro"
    site_title: str = "Ștefan Roșu"
    debug: bool = False
    host: str = "127.0.0.1"
    port: int = 8000
    homepage_news_limit: int = 5
    github_url: str = "https://github.com/rosustefan"
    linkedin_url: str = "https://www.linkedin.com/in/%C8%99tefan-andrei-ro%C8%99u-01b996118"
    twitter_url: str = "https://twitter.com/Stefan1703"

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
