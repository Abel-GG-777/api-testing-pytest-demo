# Video Script: API Testing with Pytest and FastAPI

Hello, my name is Abel. In this video, I will explain how to apply Pytest as an API Testing Framework in a FastAPI application.

API testing is the process of validating backend endpoints by sending requests and checking the responses. It verifies HTTP status codes, response data, error messages, and business behavior.

API tests are important because many applications depend on backend services. Automated tests help detect errors before deployment and make it safer to change the code.

There are several API testing frameworks. Postman and Newman are useful for creating API collections and running them from the command line. Rest Assured is popular in Java projects. Karate DSL is useful for readable, behavior-driven API scenarios. In this demo, I use Pytest because it is simple, powerful, and works very well with Python and FastAPI.

The demo API was created with FastAPI. It includes a home endpoint, a health check endpoint, a users list endpoint, a user detail endpoint, and a create user endpoint. The data is stored in memory to keep the project simple and easy to explain.

The tests were written with Pytest and FastAPI TestClient. They validate that the API returns the correct status codes and response bodies. The tests also check a successful user lookup, a not found response, successful user creation, and validation errors for invalid payloads.

To run the test suite locally, I use this command:

```powershell
pytest -v
```

This command discovers the test files and executes each test case. If all tests pass, it means the main API behavior is working as expected.

The project also includes GitHub Actions automation. The workflow installs Python 3.11, installs the dependencies from `requirements.txt`, and runs `pytest -v` automatically on every push or pull request to the main branch.

In conclusion, this project shows how Pytest can be used as a practical API testing framework for FastAPI applications. It provides real endpoint tests, clear automation, and a simple structure that can be expanded for larger projects.
