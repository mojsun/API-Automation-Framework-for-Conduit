"""
Test data payloads and constants for Conduit API tests.
Uses helpers for unique values where needed to avoid conflicts.
"""
from utils.helpers import unique_email, unique_username


# Default password used across tests (meets typical validation)
DEFAULT_PASSWORD = "Password123!"


def payload_register_user(email: str = None, username: str = None, password: str = None) -> dict:
    """Build payload for POST /api/users (register)."""
    return {
        "user": {
            "username": username or unique_username(),
            "email": email or unique_email(),
            "password": password or DEFAULT_PASSWORD,
        }
    }


def payload_login(email: str, password: str) -> dict:
    """Build payload for POST /api/users/login."""
    return {"user": {"email": email, "password": password}}


def payload_create_article(
    title: str = "Test Article",
    description: str = "A test description",
    body: str = "Article body content here.",
    tag_list: list = None,
) -> dict:
    """Build payload for POST /api/articles."""
    tag_list = tag_list or ["test", "automation"]
    return {
        "article": {
            "title": title,
            "description": description,
            "body": body,
            "tagList": tag_list,
        }
    }


def payload_update_article(
    title: str = None,
    description: str = None,
    body: str = None,
    tag_list: list = None,
) -> dict:
    """Build payload for PUT /api/articles/:slug. Only include provided fields."""
    article = {}
    if title is not None:
        article["title"] = title
    if description is not None:
        article["description"] = description
    if body is not None:
        article["body"] = body
    if tag_list is not None:
        article["tagList"] = tag_list
    return {"article": article} if article else {"article": {"title": "Updated Title"}}
