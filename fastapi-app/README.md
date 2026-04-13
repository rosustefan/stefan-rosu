# FastAPI App

This app is the in-progress migration of the personal site from Jekyll to FastAPI.

## Requirements

- Python 3.12+
- `uv`

## Setup

From `fastapi-app/`:

```powershell
uv sync
uv sync --group dev
```

The app now reads runtime settings from `app/settings.py` and optionally from a local `.env` file.

## Run The App

```powershell
uv run uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/`.

## Configuration

Supported settings currently include:

- `APP_NAME`
- `DEBUG`
- `HOST`
- `PORT`

Example `.env`:

```text
APP_NAME=stefanrosu-ro
DEBUG=false
HOST=127.0.0.1
PORT=8000
```

## Run Tests

```powershell
uv run pytest
```

## Run With Docker

Build the image:

```powershell
docker build -t stefanrosu-ro .
```

Run the container:

```powershell
docker run --rm --name stefanrosu-ro -p 8000:8000 stefanrosu-ro
```

Then open `http://127.0.0.1:8000/`.

If the container logs show `http://0.0.0.0:8000`, that is expected. The app is listening on all container interfaces, while Docker maps the port to your host on `127.0.0.1:8000`.

## Run With Docker Compose

Start the app:

```powershell
docker compose up --build
```

Run in the background:

```powershell
docker compose up --build -d
```

Stop it:

```powershell
docker compose down
```

## Current Structure

```text
app/
  main.py
  models.py
  content_utils.py
  pages.py
  posts.py
  projects.py
content/
  pages/
  posts/
  projects/
templates/
static/
tests/
Dockerfile
docker-compose.yml
```

## Current Routes

- `/`
- `/{slug}` for standalone pages
- `/blog`
- `/blog/{slug}`
- `/projects`
- `/projects/{slug}`
