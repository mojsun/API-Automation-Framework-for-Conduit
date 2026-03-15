"""
PyTest configuration and shared fixtures.
Provides API client, auth token, test user, and schema loading.
"""
import json
from pathlib import Path

import pytest

from config.settings import BASE_URL, RESPONSE_TIME_THRESHOLD_SEC
from utils.api_client import ApiClient
from utils.test_data import DEFAULT_PASSWORD, payload_register_user, payload_login


def _load_schema(name: str) -> dict:
    """Load JSON schema from schemas/ directory."""
    schema_path = Path(__file__).parent / "schemas" / f"{name}.json"
    with open(schema_path) as f:
        return json.load(f)


@pytest.fixture(scope="session")
def api_base_url():
    """Base URL for the Conduit API."""
    return BASE_URL


@pytest.fixture(scope="session")
def response_time_threshold():
    """Max allowed response time in seconds for performance checks."""
    return RESPONSE_TIME_THRESHOLD_SEC


@pytest.fixture
def client(api_base_url):
    """Fresh API client per test (no auth by default)."""
    return ApiClient(base_url=api_base_url)


@pytest.fixture
def auth_client(client):
    """
    API client with valid auth token.
    Registers a new user, logs in, and sets token on client.
    """
    payload = payload_register_user()
    email = payload["user"]["email"]
    password = payload["user"]["password"]
    username = payload["user"]["username"]

    # Register
    r = client.post("/api/users", json=payload)
    assert r.status_code == 201, f"Registration failed: {r.text}"
    data = r.json()
    assert "user" in data and "token" in data["user"]
    token = data["user"]["token"]

    client.set_auth_token(token)
    yield client
    client.clear_auth_token()


@pytest.fixture
def test_user(auth_client):
    """
    Dict with email, password, username of the authenticated test user.
    Use with auth_client when you need both token and user credentials.
    """
    # auth_client already registered a user; get current user to return consistent data
    r = auth_client.get("/api/user")
    assert r.status_code == 200
    user = r.json()["user"]
    return {
        "email": user["email"],
        "username": user["username"],
        "password": DEFAULT_PASSWORD,
    }


@pytest.fixture
def user_schema():
    """Loaded user response schema for jsonschema validation."""
    return _load_schema("user_schema")


@pytest.fixture
def article_schema():
    """Loaded article response schema for jsonschema validation."""
    return _load_schema("article_schema")


@pytest.fixture
def error_schema():
    """Loaded error response schema."""
    return _load_schema("error_schema")
