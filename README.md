# Python OCR Server

Powered by [FastAPI](https://github.com/tiangolo/fastapi) + [EasyOCR](https://github.com/JaidedAI/EasyOCR).
Specifically, FastAPI runs the API server for uploading image files and EasyOCR does the text detections.

Basic implementation to handle english text without GPU support.

## Local Run

### Update environment

- Copy or Rename `.env.example` as `.env.dev`

```sh
mv .env.example .env.dev
```

### Run with Docker

Requires [docker-compose](https://docs.docker.com/compose/install/) to be installed (this comes with Docker Desktop).

```sh
docker-compose up
# Open localhost:8000/health
```

Use `-d` to detach from logs.

Use `--build` on subsequent runs to rebuild dependencies / docker image.

*NOTE:* I had to increase Docker RAM limit on my machine to allow large images to process.

#### Lint, Check, Test with Docker

```sh
# Linting
docker-compose run backend python -m black .
docker-compose run backend python -m isort --profile=black .
docker-compose run backend python -m flake8 --config=./.flake8 .
# Unit Testing
docker-compose run backend python -m pytest

# Turn off / tear down
docker-compose down
```

### Local Python environment

For code completion / linting / developing / etc.

```sh
python -m venv venv
. ./venv/bin/activate
# .\venv\Scripts\activate for Windows
python -m pip install -r ./backend/requirements.dev.txt
pre-commit install

# Run it
cd backend
uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```

#### Lint, Check, Test with Local Python

```sh
# Should be in backend directory
cd backend

# Linting
python -m black .
python -m isort --filter-files --profile=black .
python -m flake8 --config=./.flake8 .
# Testing
python -m pytest
```

## Features

- Development Containerization with [Docker](https://docs.docker.com/)
- Dependency installation with Pip
- Linting with [pre-commit](https://pre-commit.com/) and [Flake8](https://flake8.pycqa.org/en/latest/)
- Code formatting with [Black](https://black.readthedocs.io/en/stable/) and [isort](https://github.com/PyCQA/isort)
- Testing with [pytest](https://docs.pytest.org/en/6.2.x/getting-started.html)
