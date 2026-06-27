# Applying Pytest and Requests for Real-World API Testing in a FastAPI Application

## Introduction

API testing is an essential practice for validating backend applications before they are deployed. In this project, I built a small FastAPI application and tested its endpoints using Pytest and FastAPI TestClient. The goal is to show a practical and academic example of how automated API tests can improve reliability.

## What is API Testing?

API testing verifies the behavior of application endpoints. Instead of checking visual elements, API tests send HTTP requests and validate status codes, response bodies, data formats, and error handling.

## Why API Testing is Important

Modern applications often depend on APIs to connect frontends, services, databases, and external systems. If an API endpoint fails, many parts of the system can be affected. Automated API tests help detect problems early and provide confidence when making changes.

## API Testing Frameworks Comparative

| Framework | Language / Ecosystem | Best use case | Automation support |
| --- | --- | --- | --- |
| Pytest + Requests / TestClient | Python | Developer-friendly automated API tests | Excellent with CI/CD tools |
| Postman + Newman | JavaScript / CLI ecosystem | Manual and automated API collections | Good for pipeline execution |
| Rest Assured | Java | API testing in Java projects | Strong with Maven, Gradle, and CI |
| Karate DSL | Java / DSL | BDD-style API tests with readable scenarios | Good CI/CD integration |

## Why I Chose Pytest

I chose Pytest because it is simple, readable, and widely used in Python projects. It allows developers to write test functions with plain assertions, and it integrates easily with FastAPI through TestClient.

## Demo API with FastAPI

The demo API provides endpoints for a welcome message, health check, listing users, retrieving a user by id, and creating a new user in memory.

Example from `app/main.py`:

```python
@app.get("/users/{user_id}", response_model=User)
def get_user_by_id(user_id: int) -> User:
    """Return one user by id or a clear 404 error."""
    for user in users:
        if user.id == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {user_id} was not found.",
    )
```

## Writing Real-World API Test Cases

The test suite checks successful responses, response content, list structures, user lookup, error handling, and validation failures.

Example from `tests/test_api.py`:

```python
def test_health_check_returns_ok():
    # Validates that the health endpoint reports the API as available.
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```

## Running the Tests Locally

To install dependencies and run the tests:

```powershell
python -m pip install -r requirements.txt
pytest -v
```

## Automating API Tests with GitHub Actions

GitHub Actions can run the test suite automatically when code is pushed or when a pull request is opened.

Example from `.github/workflows/api-tests.yml`:

```yaml
name: API Tests with Pytest

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  api-tests:
    runs-on: ubuntu-latest
```

## Results

The project includes seven API tests that validate the main behavior of the demo application. These tests can be executed locally with Pytest and automatically in GitHub Actions.

## Conclusion

Pytest is a strong option for API testing in Python because it is readable, flexible, and easy to automate. Combined with FastAPI and GitHub Actions, it supports a simple but effective workflow for validating backend behavior before deployment.

## GitHub Repository Link

GitHub repository: ADD_GITHUB_REPOSITORY_LINK_HERE
