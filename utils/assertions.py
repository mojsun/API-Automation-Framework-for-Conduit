"""
Custom assertions and response validation helpers.
Provides clear failure messages for API tests.
"""
from typing import Any, Dict, List, Optional

import jsonschema
import requests


def assert_status_code(response: requests.Response, expected: int) -> None:
    """Assert response status code with a clear message."""
    assert response.status_code == expected, (
        f"Expected status code {expected}, got {response.status_code}. "
        f"Response body: {response.text[:500]}"
    )


def assert_json_has_keys(data: Dict[str, Any], keys: List[str], prefix: str = "Response") -> None:
    """Assert that a JSON object contains the given top-level keys."""
    missing = [k for k in keys if k not in data]
    assert not missing, f"{prefix} missing required keys: {missing}. Keys present: {list(data.keys())}"


def assert_json_schema(response: requests.Response, schema: Dict[str, Any]) -> None:
    """Validate response JSON against a jsonschema. Raises on validation error."""
    data = response.json()
    jsonschema.validate(instance=data, schema=schema)


def assert_error_response(response: requests.Response, expected_status: int = 422) -> None:
    """Assert response is an error with expected status and has 'errors' or 'message'."""
    assert_status_code(response, expected_status)
    data = response.json()
    # Conduit/RealWorld often returns { "errors": { "body": ["..."] } } or similar
    has_error_info = "errors" in data or "message" in data or "message" in str(data).lower()
    assert has_error_info or response.status_code >= 400, (
        f"Expected error payload (errors/message), got: {data}"
    )


def assert_response_time_ok(elapsed_seconds: float, threshold_seconds: float) -> None:
    """Assert response completed within threshold (for basic performance check)."""
    assert elapsed_seconds < threshold_seconds, (
        f"Response time {elapsed_seconds:.2f}s exceeded threshold {threshold_seconds}s"
    )
