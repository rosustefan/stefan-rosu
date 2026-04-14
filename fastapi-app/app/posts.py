import logging
import re
from datetime import date as datetime_date
from pathlib import Path

from app.content_schemas import PostFrontMatter
from app.content_utils import load_markdown_document, render_markdown, resolve_slug, resolve_title
from app.models import Post

BASE_DIR = Path(__file__).resolve().parent.parent
POSTS_DIR = BASE_DIR / "content" / "posts"
POST_FILENAME_PATTERN = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.+)$")
logger = logging.getLogger(__name__)


def _slug_from_path(file_path: Path) -> str:
    match = POST_FILENAME_PATTERN.match(file_path.stem)
    slug = match.group("slug") if match else file_path.stem
    return slug.replace(" copy", "").replace(" ", "-")


def _date_from_path(file_path: Path) -> datetime_date | None:
    match = POST_FILENAME_PATTERN.match(file_path.stem)
    if not match:
        return None

    return datetime_date.fromisoformat(match.group("date"))


def build_post(file_path: Path) -> Post:
    try:
        document = load_markdown_document(file_path)
        slug = resolve_slug(document, _slug_from_path(file_path))
        metadata = PostFrontMatter.model_validate(document.metadata)
    except Exception:
        logger.exception("Failed to load post from %s", file_path)
        raise

    return Post(
        title=metadata.title or resolve_title(document, slug),
        slug=slug,
        date=document.get("date", _date_from_path(file_path)),
        summary=document.get("summary") or metadata.description or "",
        tags=metadata.tags,
        html=render_markdown(document.content),
    )


def load_post(slug: str) -> Post | None:
    if not POSTS_DIR.exists():
        logger.warning("Posts directory does not exist: %s", POSTS_DIR)
        return None

    for file_path in POSTS_DIR.glob("*.md"):
        post = build_post(file_path)
        if post.slug == slug:
            return post

    return None


def list_posts() -> list[Post]:
    if not POSTS_DIR.exists():
        logger.warning("Posts directory does not exist: %s", POSTS_DIR)
        return []

    posts = [
        build_post(file_path)
        for file_path in POSTS_DIR.glob("*.md")
    ]
    posts.sort(key=lambda post: post.date or "", reverse=True)
    return posts
