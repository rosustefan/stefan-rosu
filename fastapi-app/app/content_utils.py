from pathlib import Path

import frontmatter
from markdown import markdown


def load_markdown_document(file_path: Path) -> frontmatter.Post:
    return frontmatter.load(file_path)


def render_markdown(content: str) -> str:
    return markdown(content)


def resolve_slug(document: frontmatter.Post, fallback: str) -> str:
    return document.get("slug", fallback)


def resolve_title(document: frontmatter.Post, fallback_slug: str) -> str:
    return document.get("title", fallback_slug.replace("-", " ").title())
