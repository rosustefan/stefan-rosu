from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.errors import register_error_handlers
from app.news import list_active_news
from app.pages import load_page
from app.posts import list_posts, load_post
from app.projects import list_projects, load_project
from app.settings import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)
app.mount("/static", StaticFiles(directory=settings.static_dir), name="static")

templates = Jinja2Templates(directory=str(settings.templates_dir))
templates.env.globals["settings"] = settings
register_error_handlers(app, templates)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    page = load_page("about")
    if page is None:
        raise HTTPException(status_code=404, detail="Page not found")

    return templates.TemplateResponse(
        request=request,
        name="page.html",
        context={
            "title": page.title,
            "page": page,
            "recent_news": list_active_news()[: settings.homepage_news_limit],
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
        raise HTTPException(status_code=404, detail="Page not found")

    return templates.TemplateResponse(
        request=request,
        name="page.html",
        context={
            "title": page.title,
            "page": page,
        },
    )
