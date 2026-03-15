"""
Helper functions for test data: unique emails, usernames, and slugs.
"""
import random
import string
import time


def random_string(length: int = 8, chars: str = None) -> str:
    """Generate a random string of given length."""
    chars = chars or (string.ascii_lowercase + string.digits)
    return "".join(random.choices(chars, k=length))


def unique_email(prefix: str = "qa") -> str:
    """Generate a unique email for registration (avoids duplicate user errors)."""
    timestamp = int(time.time() * 1000)
    rnd = random_string(4)
    return f"{prefix}_{timestamp}_{rnd}@example.com"


def unique_username(prefix: str = "u") -> str:
    """Generate a unique username for registration (max 20 chars for Conduit API)."""
    # Keep under 20 chars: prefix (2) + _ + 6 digit timestamp suffix + 4 random = 14 chars
    suffix = str(int(time.time() * 1000) % 1000000).zfill(6) + random_string(4)
    return f"{prefix}_{suffix}"[:20]


def unique_article_slug(title: str) -> str:
    """Convert title to a slug-like string and make it unique (e.g. for assertions)."""
    base = title.lower().replace(" ", "-")
    allowed = "-".join(c for c in base if c.isalnum() or c == "-")
    return f"{allowed}-{random_string(6)}"
