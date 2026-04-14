from app.news import list_active_news, list_archived_news
from app.pages import load_page
from app.projects import list_projects


def test_load_about_page_includes_profile_and_subtitle():
    page = load_page("about")

    assert page is not None
    assert page.title == "About Me"
    assert "cycling through music n' emotions" in page.subtitle
    assert page.profile_image == "stefan_rosu_2026.png"


def test_list_projects_returns_migrated_projects():
    projects = list_projects()

    assert len(projects) == 3
    assert [project.title for project in projects] == [
        "Devsearch",
        "Period and Fertility Calculator",
        "The Snake Game in Rust/WASM and JS/TS",
    ]


def test_list_active_news_returns_only_homepage_items():
    active_news = list_active_news()

    assert len(active_news) == 3
    assert all(item.show_on_homepage for item in active_news)
    assert active_news[0].date >= active_news[-1].date


def test_list_archived_news_returns_non_homepage_items():
    archived_news = list_archived_news()

    assert len(archived_news) == 9
    assert all(not item.show_on_homepage for item in archived_news)


def test_news_links_are_normalized_to_fastapi_routes():
    news_items = list_active_news() + list_archived_news()

    assert any('href="/blog/rust-wasm-js-snake-game"' in item.title_html for item in news_items)
    assert any('href="/projects/period_and_fertility_calculator"' in item.title_html for item in news_items)
