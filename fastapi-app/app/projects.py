from pathlib import Path

from app.content_utils import load_markdown_document, render_markdown, resolve_slug, resolve_title
from app.models import Project

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_DIR = BASE_DIR / "content" / "projects"


def build_project(file_path: Path) -> Project:
    document = load_markdown_document(file_path)
    slug = resolve_slug(document, file_path.stem)

    return Project(
        title=resolve_title(document, slug),
        slug=slug,
        summary=document.get("summary", ""),
        status=document.get("status", ""),
        html=render_markdown(document.content),
    )


def load_project(slug: str) -> Project | None:
    project_path = PROJECTS_DIR / f"{slug}.md"
    if not project_path.exists():
        return None

    return build_project(project_path)


def list_projects() -> list[Project]:
    if not PROJECTS_DIR.exists():
        return []

    projects = [
        build_project(file_path)
        for file_path in PROJECTS_DIR.glob("*.md")
    ]
    projects.sort(key=lambda project: project.title.lower())
    return projects
