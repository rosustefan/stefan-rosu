import re
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.errors import register_error_handlers
from app.logging_config import configure_logging
from app.news import list_active_news
from app.pages import load_page
from app.posts import list_posts, load_post
from app.projects import list_projects, load_project
from app.settings import settings

configure_logging(settings.log_level)
logger = logging.getLogger(__name__)

PARAGRAPH_PATTERN = re.compile(r"(<p>.*?</p>)", re.DOTALL)


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info(
        "Starting %s on %s:%s with debug=%s",
        settings.app_name,
        settings.host,
        settings.port,
        settings.debug,
    )
    yield


app = FastAPI(title=settings.app_name, debug=settings.debug, lifespan=lifespan)
app.mount("/static", StaticFiles(directory=settings.static_dir), name="static")

templates = Jinja2Templates(directory=str(settings.templates_dir))
templates.env.globals["settings"] = settings
register_error_handlers(app, templates)


@app.get("/favicon.ico", include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse(settings.static_dir / "favicon.ico")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    page = load_page("about")
    if page is None:
        logger.warning("Home page content not found: about")
        raise HTTPException(status_code=404, detail="Page not found")

    paragraphs = PARAGRAPH_PATTERN.findall(page.html)
    story_excerpt = "".join(paragraphs[:2]) if paragraphs else page.html

    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "title": settings.site_title,
            "page": page,
            "recent_posts": list_posts()[: settings.home_writing_limit],
            "featured_projects": list_projects()[: settings.home_projects_limit],
            "recent_news": list_active_news()[: settings.homepage_news_limit],
            "story_excerpt": story_excerpt,
        },
    )


@app.get("/blog", response_class=HTMLResponse)
async def blog_index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="blog_index.html",
        context={
            "title": "Blog",
            "posts": list_posts(),
        },
    )


@app.get("/blog/{slug}", response_class=HTMLResponse)
async def blog_post(request: Request, slug: str) -> HTMLResponse:
    post = load_post(slug)
    if post is None:
        logger.warning("Blog post not found: %s", slug)
        raise HTTPException(status_code=404, detail="Post not found")

    return templates.TemplateResponse(
        request=request,
        name="post.html",
        context={
            "title": post.title,
            "post": post,
        },
    )


@app.get("/projects", response_class=HTMLResponse)
async def projects_index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="projects_index.html",
        context={
            "title": "Projects",
            "projects": list_projects(),
        },
    )


@app.get("/projects/{slug}", response_class=HTMLResponse)
async def project_detail(request: Request, slug: str) -> HTMLResponse:
    project = load_project(slug)
    if project is None:
        logger.warning("Project not found: %s", slug)
        raise HTTPException(status_code=404, detail="Project not found")

    return templates.TemplateResponse(
        request=request,
        name="project.html",
        context={
            "title": project.title,
            "project": project,
        },
    )


@app.get("/{slug}", response_class=HTMLResponse)
async def page(request: Request, slug: str) -> HTMLResponse:
    page = load_page(slug)
    if page is None:
        logger.warning("Page not found: %s", slug)
        raise HTTPException(status_code=404, detail="Page not found")

    return templates.TemplateResponse(
        request=request,
        name="page.html",
        context={
            "title": page.title,
            "page": page,
        },
    )
