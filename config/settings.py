"""
Configuration and environment settings for the API automation framework.
Base URL and optional overrides are loaded from environment variables.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from project root (parent of config/)
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=_env_path)

# API base URL - no trailing slash; paths will be appended (e.g. /api/users)
BASE_URL = os.getenv("BASE_URL", "https://conduit-api.bondaracademy.com")
# Optional: response time threshold in seconds for performance checks
RESPONSE_TIME_THRESHOLD_SEC = float(os.getenv("RESPONSE_TIME_THRESHOLD_SEC", "3.0"))
