from dataclasses import dataclass
from datetime import date as datetime_date, datetime


@dataclass(slots=True)
class Page:
    title: str
    slug: str
    html: str
    subtitle: str = ""


@dataclass(slots=True)
class Post:
    title: str
    slug: str
    html: str
    date: datetime_date | None = None
    summary: str = ""


@dataclass(slots=True)
class Project:
    title: str
    slug: str
    html: str
    summary: str = ""
    status: str = ""
    category: str = ""
    image: str = ""


@dataclass(slots=True)
class NewsItem:
    title_html: str
    body_html: str
    date: datetime
    show_on_homepage: bool = False
