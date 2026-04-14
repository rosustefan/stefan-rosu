import logging
import re
from datetime import datetime
from pathlib import Path

from app.content_utils import load_markdown_document, render_markdown
from app.models import NewsItem

BASE_DIR = Path(__file__).resolve().parent.parent
NEWS_DIR = BASE_DIR / "content" / "news"
logger = logging.getLogger(__name__)

HREF_PATTERN = re.compile(r'href="([^"]+)"')
BLOG_PATH_PATTERN = re.compile(r"^/?blog/\d{4}/(?P<slug>[^/]+)/?$")
PROJECTS_PATH_PATTERN = re.compile(r"^/?projects/(?P<slug>[^/]+)/?$")
HTML_TAG_PATTERN = re.compile(r"<[^>]+>")


def _normalize_href(href: str) -> str:
    blog_match = BLOG_PATH_PATTERN.match(href)
    if blog_match:
        return f"/blog/{blog_match.group('slug')}"

    project_match = PROJECTS_PATH_PATTERN.match(href)
    if project_match:
        return f"/projects/{project_match.group('slug')}"

    return href


def _normalize_title_links(title_html: str) -> str:
    return HREF_PATTERN.sub(lambda match: f'href="{_normalize_href(match.group(1))}"', title_html)


def _strip_html(value: str) -> str:
    return HTML_TAG_PATTERN.sub("", value).strip()


def _build_news_item(file_path: Path) -> NewsItem:
    try:
        document = load_markdown_document(file_path)
        raw_date = document.get("date")
        parsed_date = raw_date if isinstance(raw_date, datetime) else datetime.fromisoformat(str(raw_date))
        title_html = _normalize_title_links(document.get("title", ""))
        body_html = render_markdown(document.content) if document.content else ""
        if _strip_html(body_html) == _strip_html(title_html):
            body_html = ""
    except Exception:
        logger.exception("Failed to load news item from %s", file_path)
        raise

    return NewsItem(
        title_html=title_html,
        body_html=body_html,
        date=parsed_date,
        show_on_homepage=bool(document.get("show_on_homepage", False)),
    )


def _list_news() -> list[NewsItem]:
    if not NEWS_DIR.exists():
        logger.warning("News directory does not exist: %s", NEWS_DIR)
        return []

    items = [_build_news_item(file_path) for file_path in NEWS_DIR.glob("*.md")]
    items.sort(key=lambda item: item.date, reverse=True)
    return items


def list_active_news() -> list[NewsItem]:
    return [item for item in _list_news() if item.show_on_homepage]


def list_archived_news() -> list[NewsItem]:
    return [item for item in _list_news() if not item.show_on_homepage]
