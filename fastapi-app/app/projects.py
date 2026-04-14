import logging
from pathlib import Path

from app.content_utils import load_markdown_document, render_markdown, resolve_slug, resolve_title
from app.models import Project

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_DIR = BASE_DIR / "content" / "projects"
logger = logging.getLogger(__name__)


def build_project(file_path: Path) -> Project:
    try:
        document = load_markdown_document(file_path)
        slug = resolve_slug(document, file_path.stem)
    except Exception:
        logger.exception("Failed to load project from %s", file_path)
        raise

    return Project(
        title=resolve_title(document, slug),
        slug=slug,
        summary=document.get("summary") or document.get("description", ""),
        status=document.get("status", ""),
        image=document.get("img", ""),
        html=render_markdown(document.content),
    )


def load_project(slug: str) -> Project | None:
    if not PROJECTS_DIR.exists():
        logger.warning("Projects directory does not exist: %s", PROJECTS_DIR)
        return None

    for file_path in PROJECTS_DIR.glob("*.md"):
        project = build_project(file_path)
        if project.slug == slug:
            return project

    return None


def list_projects() -> list[Project]:
    if not PROJECTS_DIR.exists():
        logger.warning("Projects directory does not exist: %s", PROJECTS_DIR)
        return []

    projects = [
        build_project(file_path)
        for file_path in PROJECTS_DIR.glob("*.md")
    ]
    projects.sort(key=lambda project: project.title.lower())
    return projects
