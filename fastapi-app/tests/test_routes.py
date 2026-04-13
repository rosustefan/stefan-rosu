def test_home_page_renders(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "FastAPI migration" in response.text


def test_page_route_renders_about_content(client):
    response = client.get("/about")

    assert response.status_code == 200
    assert "This page is rendered by FastAPI" in response.text


def test_blog_index_lists_posts(client):
    response = client.get("/blog")

    assert response.status_code == 200
    assert "My First Personal Website Is Live" in response.text


def test_blog_post_route_renders_content(client):
    response = client.get("/blog/website-is-live")

    assert response.status_code == 200
    assert "Welcome to My Corner of the World-Wide-Web!" in response.text


def test_projects_index_lists_projects(client):
    response = client.get("/projects")

    assert response.status_code == 200
    assert "FastAPI Migration" in response.text


def test_project_detail_route_renders_content(client):
    response = client.get("/projects/fastapi-migration")

    assert response.status_code == 200
    assert "incremental migration from the Jekyll site to FastAPI" in response.text


def test_unknown_page_returns_404(client):
    response = client.get("/does-not-exist")

    assert response.status_code == 404
    assert "Page not found" in response.text
