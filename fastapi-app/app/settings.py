from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

APP_DIR = Path(__file__).resolve().parent
BASE_DIR = APP_DIR.parent


class Settings(BaseSettings):
    app_name: str = "stefanrosu-ro"
    blog_title: str = "Dummy to Master Programmer"
    blog_subtitle: str = "my journey as a self-taught programmer"
    site_title: str = "Ștefan Roșu"
    home_tagline: str = "Python developer. Self-taught. Still learning."
    home_now_title: str = "Now"
    home_now_body: str = (
        "Since August 2025 I have been working as a Python Developer in a real production team, "
        "building back-end microservices with FastAPI, SQLAlchemy, PostgreSQL, GitLab, ArgoCD, and GCP."
        "I am still learning new technologies and frameworks, and I am always looking for new challenges."
    )
    home_story_title: str = "Background"
    debug: bool = False
    host: str = "127.0.0.1"
    port: int = 8000
    homepage_news_limit: int = 3
    home_writing_limit: int = 3
    home_projects_limit: int = 3
    show_email: bool = True
    show_github: bool = True
    show_linkedin: bool = True
    show_twitter: bool = False
    linkedin_url: str = "https://www.linkedin.com/in/%C8%99tefan-andrei-ro%C8%99u-01b996118"
    github_url: str = "https://github.com/rosustefan"
    email_address: str = "rosu.stefan@hotmail.com"
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
