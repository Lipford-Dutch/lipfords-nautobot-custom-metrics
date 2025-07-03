"""Unit tests for task helpers."""
import pytest
from hypothesis import given
from hypothesis import strategies as st

from tasks import is_truthy


@pytest.mark.parametrize(
    "value,expected",
    [
        ("y", True),
        ("yes", True),
        ("1", True),
        ("no", False),
        ("0", False),
        (True, True),
        (False, False),
    ],
)
def test_is_truthy(value, expected):
    """Return True for truthy values and False otherwise."""
    assert is_truthy(value) is expected  # noqa: S101


@given(st.booleans())
def test_is_truthy_idempotent(b):
    """Ensure the helper is idempotent for boolean input."""
    assert is_truthy(b) is b  # noqa: S101


@given(
    st.text().filter(
        lambda s: s.lower() not in {"y", "yes", "t", "true", "on", "1", "n", "no", "f", "false", "off", "0"}
    )
)
def test_is_truthy_invalid(s):
    """Validate that invalid strings raise ``ValueError``."""
    with pytest.raises(ValueError):
        is_truthy(s)
