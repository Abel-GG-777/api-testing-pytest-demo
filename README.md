# API Testing with Pytest and FastAPI

## Objective

This project demonstrates how to apply Pytest as an API testing framework for a FastAPI application. It includes a small demo API, real endpoint tests, and GitHub Actions automation.

## What is API Testing?

API testing verifies that endpoints return the expected HTTP status codes, response bodies, data structures, and error messages. It focuses on backend behavior instead of the user interface.

## Why Pytest?

Pytest makes API tests clear, maintainable, and easy to automate. It supports simple assertions, readable test functions, fixtures, plugins, and CI/CD integration.

## Demo API Endpoints

- `GET /`
- `GET /health`
- `GET /users`
- `GET /users/{user_id}`
- `POST /users`

## Test Cases

The test suite validates the welcome endpoint, health check, user list retrieval, user lookup by id, 404 handling, successful user creation, and request validation for invalid payloads.

## Local Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run Tests

```powershell
pytest -v
```

## Run the API Locally

```powershell
uvicorn app.main:app --reload
```

After starting the server, open:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`

## GitHub Actions Automation

The workflow in `.github/workflows/api-tests.yml` runs the Pytest suite automatically on every push or pull request targeting the `main` branch.
