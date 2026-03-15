"""
Reusable API client for Conduit API.
Centralizes HTTP methods (GET, POST, PUT, DELETE) and auth header handling.
"""
import time
from typing import Any, Dict, Optional

import requests

from config.settings import BASE_URL


class ApiClient:
    """
    HTTP client for the Conduit API.
    Supports optional token-based authentication for protected endpoints.
    """

    def __init__(self, base_url: str = BASE_URL, default_headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            default_headers or {"Content-Type": "application/json", "Accept": "application/json"}
        )

    def set_auth_token(self, token: str) -> None:
        """Set Authorization header for authenticated requests."""
        self.session.headers["Authorization"] = f"Token {token}"

    def clear_auth_token(self) -> None:
        """Remove Authorization header."""
        self.session.headers.pop("Authorization", None)

    def _url(self, path: str) -> str:
        """Build full URL from path. Path should start with / (e.g. /api/users)."""
        path = path if path.startswith("/") else f"/{path}"
        return f"{self.base_url}{path}"

    def get(self, path: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        """GET request. Returns response for assertion in tests."""
        url = self._url(path)
        return self.session.get(url, params=params, **kwargs)

    def post(self, path: str, json: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        """POST request."""
        url = self._url(path)
        return self.session.post(url, json=json, **kwargs)

    def put(self, path: str, json: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        """PUT request."""
        url = self._url(path)
        return self.session.put(url, json=json, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        """DELETE request."""
        url = self._url(path)
        return self.session.delete(url, **kwargs)

    def get_with_timing(self, path: str, params: Optional[Dict[str, Any]] = None, **kwargs):
        """GET request and return (response, elapsed_seconds)."""
        url = self._url(path)
        start = time.perf_counter()
        resp = self.session.get(url, params=params, **kwargs)
        elapsed = time.perf_counter() - start
        return resp, elapsed

    def post_with_timing(self, path: str, json: Optional[Dict[str, Any]] = None, **kwargs):
        """POST request and return (response, elapsed_seconds)."""
        url = self._url(path)
        start = time.perf_counter()
        resp = self.session.post(url, json=json, **kwargs)
        elapsed = time.perf_counter() - start
        return resp, elapsed
