import uuid
from datetime import datetime, timezone
from typing import Optional


def generate_uuid() -> str:
    """Generate a unique UUID string."""
    return str(uuid.uuid4())


def get_current_iso_time() -> str:
    """Get the current time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def is_valid_iso_time(time_str: str) -> bool:
    """Check if a string is a valid ISO 8601 format."""
    try:
        datetime.fromisoformat(time_str)
        return True
    except (ValueError, TypeError):
        return False


def is_future_date(time_str: str) -> bool:
    """Check if the given ISO string represents a future date."""
    try:
        dt = datetime.fromisoformat(time_str)
        if dt.tzinfo is None:
            # If naive (no TZ), assume local time and compare with naive now
            return dt > datetime.now()
        # If aware, compare with aware now (UTC)
        return dt > datetime.now(timezone.utc)
    except (ValueError, TypeError):
        return False
