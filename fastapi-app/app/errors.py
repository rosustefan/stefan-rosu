from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException


def register_error_handlers(app: FastAPI, templates: Jinja2Templates) -> None:
    async def not_found_handler(
        request: Request,
        exc: StarletteHTTPException,
    ) -> HTMLResponse:
        return templates.TemplateResponse(
            request=request,
            name="404.html",
            context={"title": "Page Not Found"},
            status_code=404,
        )

    async def internal_server_error_handler(
        request: Request,
        exc: Exception,
    ) -> HTMLResponse:
        return templates.TemplateResponse(
            request=request,
            name="500.html",
            context={"title": "Server Error"},
            status_code=500,
        )

    app.add_exception_handler(404, not_found_handler)
    app.add_exception_handler(500, internal_server_error_handler)
