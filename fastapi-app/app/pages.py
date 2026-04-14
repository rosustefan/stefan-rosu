import logging
from pathlib import Path

from app.content_utils import load_markdown_document, render_markdown, resolve_slug, resolve_title
from app.models import Page

BASE_DIR = Path(__file__).resolve().parent.parent
PAGES_DIR = BASE_DIR / "content" / "pages"
logger = logging.getLogger(__name__)


def load_page(slug: str) -> Page | None:
    page_path = PAGES_DIR / f"{slug}.md"
    if not page_path.exists():
        logger.warning("Page file does not exist: %s", page_path)
        return None

    document = load_markdown_document(page_path)
    resolved_slug = resolve_slug(document, slug)
    profile = document.get("profile", {}) or {}

    return Page(
        title=resolve_title(document, resolved_slug),
        slug=resolved_slug,
        html=render_markdown(document.content),
        subtitle=document.get("subtitle", ""),
        profile_image=profile.get("image", ""),
    )
