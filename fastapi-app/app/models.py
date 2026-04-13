from dataclasses import dataclass
from datetime import date as datetime_date


@dataclass(slots=True)
class Page:
    title: str
    slug: str
    html: str


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
