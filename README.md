# Conduit API Automation Framework

A professional **QA API automation project** built with **Python**, **PyTest**, and **Requests** for the [Conduit API](https://conduit-api.bondaracademy.com). This framework demonstrates API test automation best practices: reusable client design, test data management, JSON schema validation, authentication flows, CRUD coverage, and HTML reporting—suitable for portfolios and technical interviews.

---

## Overview

This project automates testing of the public Conduit API (RealWorld-style). It includes:

- **Reusable API client** for GET, POST, PUT, DELETE with optional token auth
- **Structured test suites**: authentication, users, articles CRUD, and negative/error cases
- **JSON schema validation** for user and article responses
- **Test data helpers** for unique emails/usernames to avoid flaky registration tests
- **PyTest fixtures** for auth token and test user setup
- **Markers** (smoke, regression, negative) for selective test runs
- **pytest-html** reporting with a single command
- **CI-ready** layout with GitHub Actions example

---

## Tech Stack

| Tool | Purpose |
|------|--------|
| **Python 3.8+** | Runtime |
| **PyTest** | Test framework, fixtures, markers |
| **Requests** | HTTP client for API calls |
| **python-dotenv** | Environment config (e.g. base URL) |
| **pytest-html** | HTML test reports |
| **jsonschema** | Response schema validation |

---

## Project Structure

```
api-automation-framework/
├── tests/
│   ├── test_auth.py          # Register, login, get current user
│   ├── test_users.py         # User registration scenarios
│   ├── test_articles.py      # Articles CRUD + response time check
│   └── test_negative_cases.py # Unauthorized, invalid payloads, errors
├── utils/
│   ├── api_client.py         # Reusable HTTP client (GET/POST/PUT/DELETE)
│   ├── assertions.py         # Status code, keys, schema, response time
│   ├── test_data.py          # Payload builders (register, login, article)
│   └── helpers.py            # Unique email/username generation
├── schemas/
│   ├── user_schema.json      # User response schema
│   ├── article_schema.json   # Article response schema
│   └── error_schema.json     # Error response schema
├── config/
│   └── settings.py           # BASE_URL, env loading
├── .env.example
├── conftest.py               # Fixtures: client, auth_client, test_user, schemas
├── pytest.ini                # Test discovery, markers, pythonpath
├── requirements.txt
└── README.md
```

---

## Test Coverage

| Area | Tests |
|------|--------|
| **Authentication** | Register new user, login (valid), login (invalid password), get current user with token |
| **Articles CRUD** | Create article, get by slug, update article, delete article |
| **Negative** | Create article without token (401), wrong password, invalid/missing payloads |
| **Validation** | Status codes, required keys, jsonschema validation, response time on GET article |

---

## Setup and Run

### 1. Create virtual environment and install dependencies

```bash
cd "API Automation Framework for Conduit API"
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. (Optional) Environment variables

```bash
cp .env.example .env
# Edit .env to override BASE_URL or RESPONSE_TIME_THRESHOLD_SEC if needed
```

### 3. Run all tests

```bash
pytest
```

### 4. Run by marker

```bash
pytest -m smoke
pytest -m regression
pytest -m negative
```

### 5. Generate HTML report

```bash
pytest --html=report.html --self-contained-html
```

Report is written to `report.html` in the project root; open it in a browser.

---

## Quick reference – exact commands

```bash
# Setup (from project root)
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Run all tests
pytest

# Run with verbose output
pytest -v --tb=short

# Generate pytest-html report
pytest --html=report.html --self-contained-html
```

---

## Framework Design (Interview Talking Points)

- **API client**: Single `ApiClient` class with `get`, `post`, `put`, `delete` and `set_auth_token` so tests stay DRY and easy to read.
- **Config**: Base URL and thresholds in `config/settings.py` with env overrides via `.env`.
- **Fixtures**: `auth_client` registers a user, logs in, and sets the token; `test_user` exposes email/username/password for login and negative tests.
- **Test data**: `payload_register_user()`, `payload_login()`, `payload_create_article()` in `utils/test_data.py`; unique emails/usernames via `utils/helpers.py` to avoid duplicate-user failures.
- **Assertions**: Centralized in `utils/assertions.py` (status code, keys, jsonschema, response time) with clear failure messages.
- **Schemas**: JSON schemas in `schemas/` validate response structure and catch breaking API changes.

---

## Future Improvements

- Add tests for **comments**, **favorites**, and **feed** endpoints
- Add **allure** or **pytest-html** with screenshots for failure debugging
- **Data-driven tests** via `pytest.mark.parametrize` for multiple payloads
- **Docker** image to run the suite in CI without local Python setup
- **Retries** for flaky endpoints (e.g. with `pytest-rerunfailures`)

---

## Why This Project Works for QA Portfolios and Interviews

- **Real API**: Uses a public Conduit API, so anyone can run the tests without internal access.
- **Clean structure**: Clear separation of client, config, test data, assertions, and schemas—easy to walk through in an interview.
- **Best practices**: Auth handling, schema validation, negative tests, and markers show awareness of maintainability and CI.
- **Runnable and CI-ready**: One `pip install` and `pytest` command; GitHub Actions workflow demonstrates automation in a pipeline.

---

## Resume-Ready Bullet Points

- **Designed and implemented** an API test automation framework in Python using PyTest and Requests for the Conduit API, covering authentication, user registration, and full articles CRUD with reusable client and fixtures.
- **Added JSON schema validation** for user and article responses to ensure contract compliance and catch breaking changes; integrated response time checks on critical endpoints.
- **Built negative and error-path tests** (unauthorized access, invalid payloads, wrong credentials) and centralized assertions with clear failure messages to improve debugging.
- **Configured pytest-html reporting and PyTest markers** (smoke, regression, negative) for selective runs and CI-friendly execution; set up GitHub Actions workflow for automated test execution.
